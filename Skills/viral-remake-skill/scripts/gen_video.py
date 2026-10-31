#!/usr/bin/env python3
"""Default: display a prepared package. --confirm submits only already approved jobs.
Resume queries an existing task once; call again after a bounded wait if still running.
"""
import argparse
import common as c
import workflow as w

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',required=True)
    p.add_argument('--package');p.add_argument('--jobs',nargs='+');p.add_argument('--confirm',action='store_true')
    p.add_argument('--resume',help='Local task record ID, not a new create')
    a=p.parse_args()
    if a.resume:
        r=w.resume(a.run,a.resume);print(r['id'],r['status']);return
    if not a.package:p.error('Use review.py first; --package required')
    pkg=w.verify_package(a.package)
    if pkg['modality']!='video':p.error('Not a video package')
    if not a.confirm:
        for j in pkg['jobs']: print(j['id'],j['prompt'],j['settings'],j['quote'],sep='\n')
        print('No submission. Show review.html/keyframes; obtain user confirmation and record it with review.py.')
        return
    if not a.jobs:p.error('--jobs required (partial approval supported)')
    for r in w.submit(a.run,a.package,a.jobs):print(r['id'],r['task_id'],r['status'])
if __name__=='__main__':main()
