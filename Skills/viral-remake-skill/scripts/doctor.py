#!/usr/bin/env python3
"""Local diagnostics; optional explicit read-only Ark evidence collection. No inference pings."""
import argparse
import importlib.util
from pathlib import Path
import shutil
import sys
import common as c
from ark_cli import Client

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--discover',help='NEW directory for read-only raw evidence')
    p.add_argument('--profile');p.add_argument('--resource');p.add_argument('--model');p.add_argument('--model-version')
    p.add_argument('--modality',choices=['image','video','text']);a=p.parse_args()
    for executable in ('ve','ffmpeg','ffprobe'): print(executable,shutil.which(executable) or 'unavailable')
    for mod in ('yaml','PIL'):print(mod,'available' if importlib.util.find_spec(mod) else 'unavailable')
    print('Python',sys.version.split()[0]);print('Local check only; authentication and online capabilities remain unverified.')
    if not a.discover:return
    if not all((a.profile,a.resource,a.model,a.modality)):p.error('--discover needs --profile --resource --model --modality; resolve endpoint binding first using the official resources skill')
    out=Path(a.discover);out.mkdir(parents=True,exist_ok=False);out.chmod(0o700)
    client=Client()
    calls={'resource':['resources','resolve',a.resource] if a.resource.startswith('ep-') else ['resources','list','--modality',a.modality],
           'capabilities':['models','get',a.model,*(['--version',a.model_version] if a.model_version else []),'--transform','supported_params'],
           'pricing':['pricing','models','--model',a.model]}
    for name,args in calls.items():
        data=client.query(args,a.profile); c.write_new(out/(name+'.json'),data);(out/(name+'.json')).chmod(0o600)
    print('Evidence saved. Review resource binding, service/region and parameter descriptions; normalize route/pricing per references/interfaces.md.')
if __name__=='__main__':main()
