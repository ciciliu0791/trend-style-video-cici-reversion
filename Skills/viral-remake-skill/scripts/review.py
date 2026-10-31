#!/usr/bin/env python3
"""Build a review package, or record a confirmation already given by the user."""
import argparse
import workflow as w

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run',required=True);p.add_argument('--brief');p.add_argument('--modality',choices=['image','video'],default='video')
    p.add_argument('--approve',help='Exact package.json shown to user');p.add_argument('--jobs',nargs='+');p.add_argument('--evidence')
    a=p.parse_args()
    if a.approve:
        if not a.jobs or not a.evidence:p.error('--approve requires --jobs and actual user --evidence')
        w.approve(a.run,a.approve,a.jobs,a.evidence);print('Recorded confirmation for '+', '.join(a.jobs))
    else:
        if not a.brief:p.error('--brief required')
        print(w.package(a.run,a.brief,a.modality))
if __name__=='__main__': main()
