"""Versioned review packages, approvals, budget reservations and resumable tasks."""
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import html
import math
from pathlib import Path
import shutil
import uuid
import common as c
from ark_cli import Client, validate_job


def manifest(run):
    p=Path(run)/'manifest.json'
    return c.load_json(p) if p.exists() else {'schema_version':2,'storyboard':None}

def select_storyboard(run,path):
    m=manifest(run); m['storyboard']=c.file_ref(path); c.save_json(Path(run)/'manifest.json',m)

def selected_storyboard(run):
    ref=manifest(run).get('storyboard')
    if not ref: raise ValueError('No pinned storyboard; use storyboard.py --import-json')
    c.verify_file(ref); return ref['path']

def load_picks(run):
    p=Path(run)/'05_images/picks.json'
    return c.load_json(p) if p.exists() else {'character':None,'keyframes':{}}

def validate_storyboard(sb,brief,meta):
    shots=sb.get('shots',[])
    if not shots: raise ValueError('Empty storyboard')
    seen=set(); end=0.0
    for s in shots:
        if str(s['id']) in seen: raise ValueError('Duplicate shot ID')
        seen.add(str(s['id']))
        if not all(isinstance(s.get(k),(int,float)) and math.isfinite(s[k]) for k in ('start','end')): raise ValueError('Invalid shot timing')
        if abs(s['start']-end)>0.001 or s['end']<=s['start']: raise ValueError('Shot gaps, overlaps or nonpositive duration')
        for k in ('action','entry_state','exit_state','keyframe_brief'):
            if not s.get(k): raise ValueError(f'Shot {s["id"]} missing {k}')
        end=s['end']
    if abs(end-sb['duration'])>0.001: raise ValueError('Storyboard duration mismatch')
    target=brief['output']['duration']
    if target!='auto' and abs(float(target)-end)>0.001: raise ValueError('Brief duration mismatch')
    if brief['fidelity']=='close-timing':
        if meta.get('coverage')!='measured-cuts': raise ValueError('Close timing needs measured source cuts, not sampled observations')
        source=meta.get('measured_shots',[])
        if len(source)!=len(shots): raise ValueError('Close timing requires one mapped shot per measured source shot')
        for s,orig in zip(shots,source):
            if s.get('orig_shot')!=orig['id'] or max(abs(s[k]-orig[k]) for k in ('start','end'))>0.3: raise ValueError('Close timing differs by >0.3s; use adaptation or revise')
    for s in shots:
        if s.get('keyframe_from') and str(s['keyframe_from']) not in seen: raise ValueError('Unknown shared keyframe shot')
    return sb

def refs_for(brief,shot):
    refs=[]
    def add(path,role,label,invariants=''):
        refs.append({**c.file_ref(path),'role':role,'label':label,'invariants':invariants})
    chosen=shot.get('cast')
    for actor in brief['cast']:
        if chosen is None or actor['id'] in chosen:
            for path in actor.get('references',[]): add(path,'reference_image',actor['id']+' identity',actor.get('invariants',''))
    if not brief['cast'] and brief['person'].get('reference'):
        add(brief['person']['reference'],'reference_image','lead identity',brief['person'].get('invariants',''))
    if shot.get('product_visible',bool(brief['product'].get('name'))):
        for path in brief['product']['images']: add(path,'reference_image','product identity',brief['product'].get('geometry',''))
    for ref in brief['references']:
        if not ref.get('shots') or str(shot['id']) in [str(x) for x in ref['shots']]:
            add(ref['path'],ref.get('role','reference_image'),ref.get('purpose','environment/style'),ref.get('invariants',''))
    return refs

def render_prompt(shots,brief,refs,modality):
    lines=['Create an original '+('still keyframe' if modality=='image' else 'video')+' adapting the approved structure.',
           'Reference roles (identity does not imply source pose/background):']
    counters={}
    for ref in refs:
        kind='Video' if ref['role']=='reference_video' else 'Audio' if ref['role']=='reference_audio' else 'Image'
        counters[kind]=counters.get(kind,0)+1
        lines.append(f'@{kind}{counters[kind]}: {ref["label"]}; {ref["role"]}. {ref.get("invariants", "")}')
    start=shots[0]['start']
    for s in shots:
        lines += [f'Shot {s["id"]}, {s["start"]-start:g}–{s["end"]-start:g}s: {s.get("shot_type", "")}; {s.get("camera", "")}.',
                  'Entry: '+s['entry_state'], 'Action: '+s['action'], 'Exit: '+s['exit_state']]
        if modality=='image': lines.append('Composition: '+s['keyframe_brief'])
        else:
            if brief['audio'].get('generate_audio'):
                for d in c.dialogue_lines(s): lines.append(f'{d.get("speaker","voiceover")} says in {brief["copy"]["language"]}: {d["line"]}')
            elif c.dialogue_lines(s): lines.append('Dialogue is added in post; do not generate speech or speaking mouth movements.')
            if brief['text_policy']=='generated' and s.get('onscreen_text'): lines.append('On-screen text exactly: '+s['onscreen_text'])
    lines.append('Natural subject anatomy and physical contact. Preserve identity invariants and screen direction; do not mirror asymmetric markings.')
    if modality=='image' or brief['text_policy']!='generated': lines.append('No generated lettering, captions or UI; exact text is handled according to the approved edit plan.')
    if modality=='video': lines.append('Audio approach: '+str(brief['audio'].get('approach','unresolved')))
    return '\n'.join(lines)

def quote(job,pricing):
    if not pricing: return {'amount':None,'currency':None,'reason':'No verified price snapshot'}
    entry=pricing.get('jobs',{}).get(job['id'])
    if not entry: return {'amount':None,'currency':pricing.get('currency'),'reason':'No matching job quote'}
    if entry.get('request_hash')!=request_hash(job): return {'amount':None,'currency':pricing.get('currency'),'reason':'Quote does not match request hash'}
    if not pricing.get('checked_at') or not pricing.get('source') or not pricing.get('currency'): raise ValueError('Incomplete pricing snapshot')
    amount=0.0
    for item in entry.get('items',[]):
        qty,unit,rate=(item.get(k) for k in ('quantity','unit_quantity','price'))
        if any(not isinstance(x,(int,float)) or not math.isfinite(x) or x<0 for x in (qty,rate)) or not isinstance(unit,(int,float)) or not math.isfinite(unit) or unit<=0: raise ValueError('Invalid pricing units')
        if not item.get('unit') or not item.get('charge_item'): raise ValueError('Missing billing unit/charge item')
        amount+=qty/unit*rate
    if not entry.get('items'): return {'amount':None,'currency':pricing['currency'],'reason':'Empty pricing items'}
    return {'amount':round(amount,8),'currency':pricing['currency'],'checked_at':pricing['checked_at'],'source':pricing['source'],'items':entry['items']}

def request_hash(job):
    return c.digest({k:v for k,v in job.items() if k not in ('quote','digest','request_hash','approval_context')})

def build_jobs(run,brief,modality):
    sb=c.load_json(selected_storyboard(run)); meta=c.load_json(Path(run)/'01_probe/meta.json')
    validate_storyboard(sb,brief,meta)
    if brief['text_policy'] is None or not brief['audio'].get('approach'): raise ValueError('Confirm text_policy and audio.approach before production')
    if brief['text_policy']=='none' and any(s.get('onscreen_text') for s in sb['shots']): raise ValueError('Text policy none conflicts with storyboard; revise the storyboard')
    route_path=brief['routes'].get(modality)
    if not route_path: raise ValueError(f'Provide reviewed routes.{modality} snapshot')
    route=c.load_json(route_path)
    picks=load_picks(run)
    if modality=='image':
        groups=[[s] for s in sb['shots'] if not s.get('keyframe_from')]
        for s in sb['shots']:
            for key,state in s.get('keyframe_states',{}).items():
                groups.append([{**s,**state,'id':key,'keyframe_states':{},'keyframe_from':None}])
    elif brief['output']['route']=='whole': groups=[sb['shots']]
    elif brief['output']['route']=='plates': groups=[[s] for s in sb['shots']]
    else: raise ValueError('output.route must be plates or whole')
    jobs=[]
    for group in groups:
        refs=[]
        for s in group:
            if modality=='video':
                key=str(s.get('keyframe_from',s['id'])); path=picks['keyframes'].get(key)
                if not path: raise ValueError(f'Missing selected keyframe for shot {s["id"]}')
                from PIL import Image
                with Image.open(path) as im: im.verify()
                refs.append({**c.file_ref(path),'role':'first_frame' if s==group[0] else 'reference_image','label':f'Approved composition shot {s["id"]}'})
                for extra in list(s.get('transition_frames',[]))+list(s.get('keyframe_states',{})):
                    if extra not in picks.get('keyframes',{}): raise ValueError(f'Missing transition frame {extra}')
                    refs.append({**c.file_ref(picks['keyframes'][extra]),'role':'reference_image','label':f'Transition state {extra}'})
            refs.extend(refs_for(brief,s))
        # Deduplicate only identical semantic references, retaining ordering and roles.
        unique=[]
        for ref in refs:
            if ref not in unique: unique.append(ref)
        refs=unique
        if modality=='video' and brief['output'].get('use_reference_video'):
            if not meta.get('ref_video'): raise ValueError('Reference video unavailable; choose a supported source clip explicitly')
            refs.append({**c.file_ref(meta['ref_video']),'role':'reference_video','label':'Structure only; exclude original identities, text and music'})
        if modality=='image': settings=dict(brief['output'].get('image_settings',{}))
        else:
            duration=group[0].get('generation_duration',group[-1]['end']-group[0]['start']) if len(group)==1 else group[-1]['end']-group[0]['start']
            if int(duration)!=duration: raise ValueError('Set whole-second generation_duration per plate for fractional edits' if len(group)==1 else 'Whole clip duration must be integral')
            settings={'duration':int(duration),'ratio':brief['output'].get('ratio',meta.get('ratio')),'resolution':brief['output']['resolution'],'generate_audio':brief['audio'].get('generate_audio',False)}
            settings.update(group[0].get('video_settings',{}) if len(group)==1 else brief['output'].get('video_settings',{}))
        jid=('KF-' if modality=='image' else 'S-')+str(group[0]['id']) if len(group)==1 else 'whole'
        if modality=='video' and settings['duration']<group[-1]['end']-group[0]['start']:
            raise ValueError('Generation duration cannot cover selected timeline range')
        job={'id':jid,'shot_ids':[str(s['id']) for s in group],'modality':modality,'route':route,'settings':settings,'references':refs,
             'prompt':render_prompt(group,brief,refs,modality),'storyboard':group,'text_policy':brief['text_policy'],'audio':brief['audio'],
             'fidelity':brief['fidelity'],'mode':brief['mode']}
        validate_job(job);job['request_hash']=request_hash(job); jobs.append(job)
    return jobs

def package(run,brief_path,modality):
    brief=c.load_brief(brief_path); jobs=build_jobs(run,brief,modality)
    pricing=c.load_json(brief['pricing']) if brief['pricing'] else None
    for j in jobs:
        j['quote']=quote(j,pricing); j['approval_context']={'budget':brief['budget'],'takes':int(brief['output']['takes'])}; j['digest']=c.digest(j)
    pkg={'schema_version':2,'created_at':c.now(),'modality':modality,'brief':c.file_ref(brief_path),'storyboard':manifest(run)['storyboard'],
         'budget':brief['budget'],'takes':int(brief['output']['takes']),'jobs':jobs}
    if pkg['takes']<1: raise ValueError('takes must be positive')
    name=c.digest(pkg)[:16]; directory=Path(run)/'reviews'/name; directory.mkdir(parents=True)
    c.write_new(directory/'package.json',pkg)
    show_package(directory,pkg)
    return directory/'package.json'

def show_package(directory,pkg):
    lines=['# '+pkg['modality'].title()+' review package','',f'Planned tasks: {len(pkg["jobs"])*pkg["takes"]}',
           'Approval must reference this package and selected job IDs. Unknown prices block submission.','']
    images=[];labels=[]
    for j in pkg['jobs']:
        lines += [f'## {j["id"]} — shots {", ".join(j["shot_ids"])}',f'Request hash: `{j["request_hash"]}`',
                  f'Settings: `{json_text(j["settings"])}`',f'Route: `{j["route"]["service"]} / {j["route"]["region"]} / {j["route"]["resource"]}`',
                  f'Cost per task: {j["quote"]["amount"]} {j["quote"]["currency"]}',f'Text: {j["text_policy"]}; audio: {json_text(j["audio"])}','', '### Exact prompt','',j['prompt'],'','### Ordered references','']
        for n,r in enumerate(j['references'],1):
            lines.append(f'{n}. {r["label"]} ({r["role"]}) — [{Path(r["path"]).name}]({r["path"]})')
            if r['role'] in ('first_frame','reference_image'):
                images.append(r['path']);labels.append(j['id']+' #'+str(n))
        lines += ['', '### Timed storyboard', '', '```json',json_text(j['storyboard'],indent=2),'```','']
    (directory/'review.md').write_text('\n'.join(lines),encoding='utf-8')
    if images:
        from probe import contact_sheet
        contact_sheet(images,str(directory/'contact.jpg'),labels,tile=320,cols=4)
    # HTML provides full-resolution images and exact prompts without Markdown renderer assumptions.
    blocks=['<!doctype html><meta charset="utf-8"><title>Remake review</title><style>body{max-width:1000px;margin:32px auto;font:16px system-ui}img{max-width:100%}pre{white-space:pre-wrap}</style>', '<h1>Review before generation</h1>']
    if images: blocks.append('<img src="contact.jpg" alt="Numbered reference contact sheet">')
    blocks.append('<pre>'+html.escape('\n'.join(lines))+'</pre>')
    for label,path in zip(labels,images): blocks.append('<h3>'+html.escape(label)+'</h3><a href="'+Path(path).as_uri()+'"><img src="'+Path(path).as_uri()+'"></a>')
    (directory/'review.html').write_text('\n'.join(blocks),encoding='utf-8')

def json_text(x,**kwargs):
    import json
    return json.dumps(x,ensure_ascii=False,**kwargs)

def verify_package(path):
    pkg=c.load_json(path)
    for k in ('brief','storyboard'): c.verify_file(pkg[k])
    for job in pkg['jobs']:
        if job['digest']!=c.digest({k:v for k,v in job.items() if k!='digest'}): raise ValueError('Package changed after rendering')
        if job.get('approval_context')!={'budget':pkg['budget'],'takes':pkg['takes']}: raise ValueError('Package batch/budget changed')
        validate_job(job)
    # Rebuild current requests: changed picks, route snapshots or brief values cannot slip through.
    current=build_jobs(Path(path).parents[2],c.load_brief(pkg['brief']['path']),pkg['modality'])
    if [j['request_hash'] for j in current]!=[j['request_hash'] for j in pkg['jobs']]: raise ValueError('Current inputs differ; render and review a new package')
    return pkg

def assert_run(run,path):
    if Path(path).resolve().parents[2]!=Path(run).resolve(): raise ValueError('Package belongs to another run; cannot split its budget ledger')

def approve(run,path,ids,evidence):
    assert_run(run,path)
    if not evidence.strip(): raise ValueError('Record the actual user confirmation text/message reference')
    pkg=verify_package(path)
    selected=[j for j in pkg['jobs'] if j['id'] in ids]
    if len(selected)!=len(set(ids)): raise ValueError('Unknown job IDs')
    if not selected: raise ValueError('Select at least one job')
    for j in selected:
        record={'job':j['id'],'digest':j['digest'],'package':str(Path(path).resolve()),'package_hash':c.file_hash(path),'evidence':evidence,'confirmed_at':c.now()}
        c.write_new(Path(run)/'approvals'/(uuid.uuid4().hex+'.json'),record)

def approved(run,job):
    return any(c.load_json(p).get('digest')==job['digest'] for p in (Path(run)/'approvals').glob('*.json'))

@contextmanager
def run_lock(run):
    Path(run).mkdir(parents=True,exist_ok=True)
    with (Path(run)/'.submission.lock').open('a') as f:
        try: fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError: raise ValueError('Another submission is active in this run')
        try: yield
        finally: fcntl.flock(f,fcntl.LOCK_UN)

def tasks(run): return [c.load_json(p) for p in sorted((Path(run)/'tasks').glob('*.json'))]

def reserve_check(run,pkg,jobs):
    budget=pkg['budget']; cap=budget.get('cap'); currency=budget.get('currency')
    if not budget.get('authorization'): raise ValueError('Missing budget authorization evidence')
    if not isinstance(cap,(int,float)) or not math.isfinite(cap) or cap<=0 or not currency: raise ValueError('Set a positive monetary cap and currency')
    existing=tasks(run); total=budget.get('external_reserve',0.0)
    if not isinstance(total,(int,float)) or not math.isfinite(total) or total<0: raise ValueError('Invalid external reserve')
    if any(t['status'] in ('submitting','submission-unknown') for t in existing): raise ValueError('Unreconciled submission; recover original task before new creates')
    for t in existing:
        if t['currency']!=currency: raise ValueError('Mixed currencies in run ledger')
        total+=t['settled'] if t.get('settled') is not None else t['reserved']
    for j in jobs:
        q=j['quote']
        if q['amount'] is None or q['currency']!=currency: raise ValueError('Unknown price/currency: obtain matching price snapshot')
        previous=[t for t in existing if t['job']==j['id'] and t['modality']==j['modality'] and t['status']!='reconciled-no-task']
        if any(t['status'] in ('queued','running','download-pending') for t in previous): raise ValueError('Existing task pending; resume instead')
        # A package approval authorizes one planned batch, never repeated invocations of that batch.
        if any(t.get('job_digest')==j['digest'] for t in previous): raise ValueError('This reviewed request was already submitted; resume or prepare a reviewed repair')
        if len(previous)+pkg['takes']>int(budget.get('max_attempts_per_job',2)): raise ValueError('Per-job attempt allowance exhausted')
        total+=q['amount']*pkg['takes']
    if total>cap+1e-9: raise ValueError('Budget cap exceeded including pending reservations')

def submit(run,path,ids,client=None):
    assert_run(run,path)
    client=client or Client()
    with run_lock(run):
        pkg=verify_package(path); selected=[j for j in pkg['jobs'] if j['id'] in ids]
        if not selected or len(selected)!=len(set(ids)): raise ValueError('Unknown/empty job selection')
        for j in selected:
            if not approved(run,j): raise ValueError(f'User confirmation missing for {j["id"]}')
        reserve_check(run,pkg,selected)
        # Run all read-only checks before the first create; repeat inside adapter immediately before create.
        for j in selected: client.live_check(j['route'])
        results=[]
        for j in selected:
            for _ in range(pkg['takes']):
                rid=uuid.uuid4().hex; out=Path(run)/'outputs'/rid; out.mkdir(parents=True); out.chmod(0o700)
                record={'id':rid,'job':j['id'],'job_digest':j['digest'],'modality':j['modality'],'route':j['route'],
                        'status':'submitting','task_id':None,'reserved':j['quote']['amount'],'currency':j['quote']['currency'],
                        'estimate':j['quote'],'usage':None,'usage_estimate':None,'settled':None,'output_dir':str(out.resolve()),'created_at':c.now()}
                state=Path(run)/'tasks'/(rid+'.json'); c.write_new(state,record)
                try:
                    result=client.generate(j,out)
                    task_id=result.get('task_id') or result.get('id')
                    if j['modality']=='video' and not task_id: raise ValueError('No task ID returned')
                    record.update(task_id=task_id,status=result.get('status','queued'))
                    c.save_json(state,record) # durable ID before next task or artifact handling
                    c.write_new(out/'response.json',result); (out/'response.json').chmod(0o600)
                    update_result(record,result); c.save_json(state,record)
                except BaseException:
                    if not record.get('task_id') and record['status']=='submitting': record['status']='submission-unknown'
                    elif record.get('task_id'): record['status']='download-pending' if record['status']=='succeeded' else record['status']
                    c.save_json(state,record)
                    raise
                results.append(record)
        return results

def update_result(record,result):
    record['usage']=result.get('usage',record.get('usage'))
    items=record.get('estimate',{}).get('items',[])
    usage=record.get('usage') or {}
    if items and all(item.get('usage_key') in usage for item in items):
        record['usage_estimate']=sum(usage[item['usage_key']]/item['unit_quantity']*item['price'] for item in items)
    record['status']=result.get('status',record['status'])
    path=result.get('local_path') or next(iter(result.get('local_paths') or []),None)
    if path and Path(path).is_file():
        if record['modality']=='video': c.ffprobe(path)
        else:
            from PIL import Image
            with Image.open(path) as im: im.verify()
        source=Path(path).resolve(); dest=Path(record['output_dir'])/('frozen'+source.suffix)
        if source!=dest.resolve():
            if dest.exists():
                if c.file_hash(source)!=c.file_hash(dest): raise ValueError('Original output differs from frozen file')
            else: shutil.copyfile(source,dest)
        record['file']=c.file_ref(dest)
    if record['status']=='succeeded' and not record.get('file'): record['status']='download-pending'

def resume(run,record_id,client=None):
    client=client or Client()
    with run_lock(run):
        state=Path(run)/'tasks'/(record_id+'.json'); record=c.load_json(state)
        if not record.get('task_id'): raise ValueError('No known task ID; reconcile evidence, never guess a recent task')
        result=client.get(record['task_id'],record['route'])
        # Preserve the response privately for signed-URL download recovery.
        poll_path=Path(record['output_dir'])/('poll-'+uuid.uuid4().hex+'.json')
        c.write_new(poll_path,result);poll_path.chmod(0o600)
        update_result(record,result);c.save_json(state,record);return record
