"""Explicit Ark CLI adapter. No HTTP model fallback or automatic create retries.
Read current upstream Ark skills before live use. Route snapshots are reviewed evidence,
not a substitute for account authentication or service-side validation.
"""
import json
import os
from pathlib import Path
import re
import subprocess
import common as c

class CLIError(RuntimeError): pass

def caller_env():
    env=os.environ.copy()
    for key in ('VE_CALLER_NAME','VE_SKILL_NAME'):
        if not env.get(key): raise CLIError(f'Set {key} from the actual host / active Volcengine skill')
    env['VE_CALLER_TYPE']='ai_agent'
    for key in ('ARKCLI_CALLER_TYPE','ARKCLI_CALLER_NAME','ARKCLI_SKILL_NAME','ARKCLI_NO_UPDATE_NOTIFIER'):
        env.pop(key,None)
    return env

class Client:
    def __init__(self, runner=None): self.runner=runner or subprocess.run; self.checked=False
    def check_version(self):
        if self.checked: return
        r=self.runner(['ve','version'],env=caller_env(),capture_output=True,text=True,check=True,timeout=30)
        m=re.search(r'(\d+)\.(\d+)\.(\d+)',r.stdout)
        if not m or tuple(map(int,m.groups()))<(1,1,11): raise CLIError('ve >= 1.1.11 required')
        self.checked=True
    def call(self,args,profile=None,timeout=600):
        self.check_version()
        cmd=['ve','arkcli',*args]
        if profile:
            if args[0].startswith('+'): cmd=['ve','arkcli',args[0],'--profile',profile,*args[1:]]
            else: cmd += ['--profile',profile]
        try:
            r=self.runner(cmd,env=caller_env(),capture_output=True,text=True,timeout=timeout)
        except subprocess.TimeoutExpired as e:
            raise CLIError('CLI timed out; creation outcome may be unknown. Do not resubmit.') from e
        if r.returncode:
            # Do not echo stderr: provider errors may contain signed URLs or credentials.
            raise CLIError(f'Ark CLI failed (exit {r.returncode}); inspect locally with redaction; no automatic retry')
        try: return json.loads(r.stdout)
        except ValueError as e: raise CLIError('Non-JSON CLI response; creation outcome may be unknown') from e
    def query(self,args,profile=None): return self.call([*args,'--format','json'],profile)
    def live_check(self,route):
        validate_route(route)
        r=self.query(['resources','resolve',route['resource']],route['profile']) if route['resource'].startswith('ep-') else self.query(['resources','list','--modality',route['modality']],route['profile'])
        entries=r.get('items') if isinstance(r,dict) else None
        if entries is not None:
            entries=[x for x in entries if x.get('id')==route['resource']]
            if len(entries)!=1: raise CLIError('Selected resource absent/ambiguous; refresh route evidence')
            r=entries[0]
        # Snapshot comparison is deliberately conservative: routing changes need a new review.
        expected=c.load_json(route['resource_evidence']['path'])
        if isinstance(expected,dict) and 'items' in expected:
            expected=next((x for x in expected['items'] if x.get('id')==route['resource']),None)
        if r != expected: raise CLIError('Resource evidence changed; refresh capabilities and review package')
    def generate(self,job,directory):
        route=job['route']; self.live_check(route)
        args=['+gen','--model',route['resource'],'--modality',job['modality'],'--format','json','--no-open','--save-to',str(directory)]
        for k,v in job['settings'].items():
            args.append('--'+k.replace('_','-')+'='+str(v).lower() if isinstance(v,bool) else '--'+k.replace('_','-')+'='+str(v))
        if route['transport']=='inline-local': args.append('--inline-local')
        for ref in job['references']: args += ['--input',ref['role']+':@'+ref['path']]
        args.append(job['prompt'])
        return self.call(args,route['profile'])
    def get(self,task_id,route):
        return self.query(['gen','get',task_id],route['profile'])
    def analyze(self,prompt,inputs,route,directory):
        for path in inputs:
            ext=Path(path).suffix.lower()
            kind='image' if ext in ('.jpg','.jpeg','.png','.webp') else 'video' if ext in ('.mp4','.mov','.webm','.mkv') else 'audio' if ext in ('.mp3','.wav','.m4a') else 'file'
            if kind not in route.get('input_modalities',[]):raise ValueError('Analysis input capability unverified: '+kind)
        self.live_check(route)
        args=['+chat','--model',route['resource'],'--format','json','--no-progress']
        for path in inputs: args += ['--input','@'+str(Path(path).resolve())]
        args.append(prompt)
        result=self.call(args,route['profile'])
        c.write_new(Path(directory)/'response.json',result)
        if result.get('status')=='incomplete': raise CLIError('Incomplete analysis saved; no automatic retry')
        content=result.get('content')
        if not isinstance(content,str): raise CLIError('Unexpected chat response saved; inspect content locally')
        try: return json.loads(content.strip().removeprefix('```json').removesuffix('```').strip())
        except ValueError as e: raise CLIError('Invalid model JSON saved; repair locally or explicitly request another run') from e

def validate_route(route):
    required=('service','profile','region','base_url','resource','model','model_version','modality','transport','checked_at','params','input_roles','resource_evidence','capability_evidence','constraints_reviewed')
    if any(k not in route for k in required): raise ValueError('Incomplete route snapshot; see references/interfaces.md')
    if route['service']!='volcengine': raise ValueError('This adapter targets Volcengine Ark; BytePlus requires a separately verified CLI route')
    if route['constraints_reviewed'] is not True: raise ValueError('Review parameter descriptions and conditional constraints first')
    if route['transport'] not in ('inline-local','tos'): raise ValueError('Unsupported reference transport')
    if not route['profile'] or not route['region'] or not route['base_url'].startswith('https://'): raise ValueError('Missing verified routing context')
    for k in ('resource_evidence','capability_evidence'): c.verify_file(route[k])
    evidence=c.load_json(route['resource_evidence']['path'])
    candidates=evidence.get('items',[]) if isinstance(evidence,dict) and 'items' in evidence else [evidence]
    matching=[x for x in candidates if isinstance(x,dict) and route['resource'] in json.dumps(x)]
    if len(matching)!=1: raise ValueError('Selected resource missing or ambiguous in evidence')
    if matching[0].get('invocable') is False: raise ValueError('Resource explicitly not invocable')

def validate_job(job):
    r=job['route']; validate_route(r)
    if r['modality']!=job['modality']: raise ValueError('Route modality mismatch')
    for k,v in job['settings'].items():
        spec=r['params'].get(k)
        if not spec or spec.get('support') is not True: raise ValueError(f'Unsupported parameter: {k}')
        if spec.get('enum') and v not in spec['enum']: raise ValueError(f'Unsupported {k}: {v}')
        if isinstance(v,(float,int)) and not isinstance(v,bool):
            if spec.get('min') is not None and v<spec['min']: raise ValueError(f'{k} below minimum')
            if spec.get('max') is not None and v>spec['max']: raise ValueError(f'{k} above maximum')
    if len(job['references'])>r.get('max_references',len(job['references'])): raise ValueError('Too many references')
    for ref in job['references']:
        c.verify_file(ref)
        if ref['role'] not in r['input_roles']: raise ValueError('Unsupported reference role')
        if r['transport']=='inline-local' and ref['role'] in ('reference_video','reference_audio'): raise ValueError('Inline transport cannot carry video/audio')
