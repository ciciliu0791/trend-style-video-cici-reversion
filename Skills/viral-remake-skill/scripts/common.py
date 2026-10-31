"""Offline helpers. No implicit credentials, defaults, uploads or model requests."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
from datetime import datetime, timezone

SKILL_DIR = str(Path(__file__).resolve().parent.parent)
PROMPT_DIR = str(Path(SKILL_DIR) / 'prompts')

def now():
    return datetime.now(timezone.utc).isoformat()

def load_env():
    """Compatibility no-op: credentials belong to the selected Ark profile."""

def load_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def save_json(path, obj):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + '.tmp')
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    os.replace(tmp, p)

def no_overwrite(path):
    if Path(path).exists():
        raise ValueError(f'Output exists: {path}; choose a new version/run')

def write_new(path, obj):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.flush(); os.fsync(f.fileno())

def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False, allow_nan=False).encode()).hexdigest()

def file_hash(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''): h.update(block)
    return h.hexdigest()

def file_ref(path):
    p = Path(path).resolve()
    if not p.is_file(): raise ValueError(f'Missing local file: {p}')
    return {'path': str(p), 'sha256': file_hash(p)}

def verify_file(ref):
    if file_hash(ref['path']) != ref['sha256']:
        raise ValueError(f'Changed file; rebuild and review: {ref["path"]}')

def step_dir(run, name):
    p = Path(run) / name; p.mkdir(parents=True, exist_ok=True); return str(p)

def log(run, **record):
    Path(run).mkdir(parents=True, exist_ok=True)
    with (Path(run)/'runlog.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps({'ts': now(), **record}, ensure_ascii=False) + '\n')
        f.flush(); os.fsync(f.fileno())

def read_prompt(name):
    return (Path(PROMPT_DIR)/name).read_text(encoding='utf-8')

def ffprobe(path):
    d = json.loads(subprocess.run(['ffprobe','-v','error','-print_format','json','-show_format','-show_streams',str(path)], capture_output=True, text=True, check=True).stdout)
    v = next(s for s in d['streams'] if s['codec_type']=='video')
    w,h = int(v['width']),int(v['height'])
    for sd in v.get('side_data_list',[]):
        if abs(int(sd.get('rotation',0))) in (90,270): w,h=h,w
    n,den = (v.get('avg_frame_rate') or '0/1').split('/')
    return {'path':str(path),'width':w,'height':h,'duration':float(d['format']['duration']),
            'fps':float(n)/float(den) if float(den) else 0,'has_audio':any(s['codec_type']=='audio' for s in d['streams']),
            'streams':d['streams'],'size_bytes':Path(path).stat().st_size}

def ratio_label(w,h):
    return min({'9:16':9/16,'3:4':3/4,'1:1':1,'4:3':4/3,'16:9':16/9,'21:9':21/9},key=lambda x:abs(w/h-float(x.split(':')[0])/float(x.split(':')[1])))

def dialogue_lines(shot):
    d=shot.get('dialogue') or []
    return [x for x in (d if isinstance(d,list) else [d]) if isinstance(x,dict) and x.get('line')]

def load_brief(path):
    import yaml
    p=Path(path).resolve(); b=yaml.safe_load(p.read_text(encoding='utf-8')) or {}
    def absolute(s): return str((p.parent/s).resolve()) if s else None
    b.setdefault('mode','ad' if b.get('product',{}).get('name') else 'creative')
    b.setdefault('fidelity','adaptation')
    b.setdefault('quality','balanced')
    b.setdefault('text_policy',None)
    b.setdefault('audio',{})
    b.setdefault('budget',{})
    b.setdefault('routes',{})
    b.setdefault('pricing',None)
    b.setdefault('copy',{}).setdefault('language','English')
    b['copy'].setdefault('cta','')
    prod=b.setdefault('product',{})
    prod['images']=[absolute(x) for x in prod.get('images',[])]
    person=b.setdefault('person',{}) or {}; b['person']=person
    person['reference']=absolute(person.get('reference'))
    b.setdefault('cast',[])
    for cast in b['cast']: cast['references']=[absolute(x) for x in cast.get('references',[])]
    b.setdefault('references',[])
    for ref in b['references']: ref['path']=absolute(ref['path'])
    b['routes']={k:absolute(v) for k,v in b['routes'].items()}
    b['pricing']=absolute(b['pricing'])
    o=b.setdefault('output',{})
    for k,v in {'duration':'auto','resolution':'720p','takes':1,'route':'plates','use_reference_video':False}.items(): o.setdefault(k,v)
    if b['mode'] not in ('ad','creative') or b['fidelity'] not in ('adaptation','close-timing'):
        raise ValueError('mode must be ad/creative; fidelity adaptation/close-timing')
    if b['text_policy'] not in (None,'generated','post','none'): raise ValueError('Invalid text_policy')
    return b
