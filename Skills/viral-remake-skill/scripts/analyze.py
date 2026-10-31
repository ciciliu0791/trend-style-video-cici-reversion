#!/usr/bin/env python3
"""Import documented analysis, or explicitly request one Ark multimodal analysis."""
import argparse
from pathlib import Path
import common as c
from ark_cli import Client

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',required=True);p.add_argument('--brief',required=True)
    g=p.add_mutually_exclusive_group(required=True);g.add_argument('--import-json');g.add_argument('--generate',action='store_true')
    p.add_argument('--analysis-budget-authorization');a=p.parse_args();b=c.load_brief(a.brief)
    dest=Path(a.run)/'02_analysis/analysis.json';c.no_overwrite(dest)
    meta=c.load_json(Path(a.run)/'01_probe/meta.json');tr=c.load_json(Path(a.run)/'01_probe/transcript.json')
    if a.import_json:an=c.load_json(a.import_json)
    else:
        if not a.analysis_budget_authorization:p.error('Paid analysis requires --analysis-budget-authorization')
        route=c.load_json(b['routes']['text']);inputs=[meta['analysis_video']] if meta.get('analysis_video') else []
        evidence=c.load_json(Path(a.run)/'01_probe/observations.json') if meta.get('coverage')=='sampled-observations' else c.load_json(Path(a.run)/'01_probe/shots.json')
        prompt=c.read_prompt('analysis.md')+'\nSOURCE:\n'+__import__('json').dumps(evidence,ensure_ascii=False)+'\nTRANSCRIPT:\n'+__import__('json').dumps(tr,ensure_ascii=False)
        out=Path(a.run)/'02_analysis/response';out.mkdir(parents=True,exist_ok=False)
        an=Client().analyze(prompt,inputs,route,out)
        c.log(a.run,step='analysis',authorization=a.analysis_budget_authorization,cost=None,response=str(out/'response.json'))
    an['coverage']=meta.get('coverage','unknown');an['transcript_available']=tr.get('available',False)
    if b['fidelity']=='close-timing' and an['coverage']!='measured-cuts':raise ValueError('Cannot claim close timing from sampled evidence')
    c.write_new(dest,an);dest.with_suffix('.md').write_text('# Source analysis\n\n```json\n'+__import__('json').dumps(an,ensure_ascii=False,indent=2)+'\n```\n',encoding='utf-8')
    print(dest)
if __name__=='__main__':main()
