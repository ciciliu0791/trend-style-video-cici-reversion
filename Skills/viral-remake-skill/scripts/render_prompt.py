#!/usr/bin/env python3
"""Render a versioned exact-prompt/keyframe review package offline."""
import argparse
from workflow import selected_storyboard as latest_storyboard, load_picks, package

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',required=True);p.add_argument('--brief',required=True)
    p.add_argument('--modality',choices=['image','video'],default='video');a=p.parse_args()
    print(package(a.run,a.brief,a.modality))
if __name__=='__main__':main()
