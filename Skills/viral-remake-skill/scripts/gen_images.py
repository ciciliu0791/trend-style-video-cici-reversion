#!/usr/bin/env python3
"""Generate budget-authorized review images, or select existing images offline.
Use review.py --modality image first. Images do not authorize video generation.
"""
import argparse
from pathlib import Path
import common as c
import workflow as w

def do_pick(run,items):
    from PIL import Image
    picks=w.load_picks(run)
    for item in items:
        key,path=item.split('=',1); path=str(Path(path).resolve())
        with Image.open(path) as im: im.verify()
        if key=='character':picks['character']=path
        else:picks['keyframes'][key.removeprefix('shot')]=path
    c.save_json(Path(run)/'05_images/picks.json',picks)
    c.log(run,step='pick',picks=picks)
    print('Picks updated. Prepare a new video review package.')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',required=True);p.add_argument('--pick',nargs='+')
    p.add_argument('--package');p.add_argument('--jobs',nargs='+');p.add_argument('--confirm',action='store_true')
    a=p.parse_args()
    if a.pick:return do_pick(a.run,a.pick)
    if not a.package:p.error('Provide --pick or an image --package')
    pkg=w.verify_package(a.package)
    if pkg['modality']!='image':p.error('Not an image package')
    if not a.confirm:
        for j in pkg['jobs']:print(j['id'],j['prompt'],j['quote'],sep='\n')
        return
    if not a.jobs:p.error('--jobs required')
    for r in w.submit(a.run,a.package,a.jobs):print(r['id'],r['status'],r.get('file'))
if __name__=='__main__':main()
