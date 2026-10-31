#!/usr/bin/env python3
"""Reconcile uncertain submissions or attach/download an existing output; never creates media."""
import argparse
import math
from pathlib import Path
import shutil
import urllib.request
import common as c
import workflow as w

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',required=True);p.add_argument('--record',required=True)
    p.add_argument('--evidence',required=True,help='Actual provider/account/review evidence, not a guess')
    g=p.add_mutually_exclusive_group(required=True)
    g.add_argument('--task-id');g.add_argument('--no-task-created',action='store_true');g.add_argument('--file')
    g.add_argument('--download-response',help='Saved response JSON belonging to this task; GET artifact only')
    g.add_argument('--settled',type=float)
    a=p.parse_args()
    with w.run_lock(a.run):
        state=Path(a.run)/'tasks'/(a.record+'.json');r=c.load_json(state)
        if a.task_id:
            if r.get('task_id') or r['status'] not in ('submitting','submission-unknown'):raise ValueError('Only reconcile an unknown creation')
            r.update(task_id=a.task_id,status='queued')
        elif a.no_task_created:
            if r.get('task_id') or r['status'] not in ('submitting','submission-unknown'):raise ValueError('Only reconcile an unknown creation')
            r.update(status='reconciled-no-task',reserved=0,settled=0)
        elif a.settled is not None:
            if not math.isfinite(a.settled) or a.settled<0:raise ValueError('Invalid settlement')
            r['settled']=a.settled
        else:
            if a.file:
                src=Path(a.file);dest=Path(r['output_dir'])/('recovered-'+src.name);c.no_overwrite(dest);shutil.copyfile(src,dest)
            else:
                response_path=Path(a.download_response).resolve()
                if response_path.parent!=Path(r['output_dir']).resolve():raise ValueError('Use a saved response inside this task output directory')
                response=c.load_json(response_path)
                if r.get('task_id') and (response.get('task_id') or response.get('id')) not in (None,r['task_id']):raise ValueError('Task ID mismatch')
                url=response.get('output_url') or response.get('content',{}).get('video_url')
                if not url or not url.startswith('https://'):raise ValueError('No HTTPS artifact URL; query original task again')
                dest=Path(r['output_dir'])/('recovered.mp4' if r['modality']=='video' else 'recovered.png');c.no_overwrite(dest)
                partial=dest.with_suffix(dest.suffix+'.part')
                with urllib.request.urlopen(url,timeout=120) as source, partial.open('xb') as target:shutil.copyfileobj(source,target)
                partial.rename(dest)
            w.update_result(r,{'status':'succeeded','local_path':str(dest)})
        r.setdefault('recovery',[]).append({'at':c.now(),'evidence':a.evidence})
        c.save_json(state,r);print(r['id'],r['status'])
if __name__=='__main__':main()
