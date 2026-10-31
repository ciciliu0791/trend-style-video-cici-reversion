#!/usr/bin/env python3
"""Import or generate a storyboard; validate and explicitly pin its version."""
import argparse
from pathlib import Path
import common as c
import workflow as w
from ark_cli import Client

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',required=True);p.add_argument('--brief',required=True)
    g=p.add_mutually_exclusive_group(required=True);g.add_argument('--import-json');g.add_argument('--generate',action='store_true')
    p.add_argument('--tag',required=True);p.add_argument('--notes',default='');p.add_argument('--analysis-budget-authorization')
    a=p.parse_args();b=c.load_brief(a.brief);meta=c.load_json(Path(a.run)/'01_probe/meta.json')
    if not a.tag.replace('-','').replace('_','').isalnum():p.error('tag: letters/digits/hyphen/underscore only')
    dest=Path(a.run)/'03_storyboard'/('storyboard-'+a.tag+'.json');c.no_overwrite(dest)
    if a.import_json:sb=c.load_json(a.import_json)
    else:
        if not a.analysis_budget_authorization:p.error('Paid storyboard generation requires --analysis-budget-authorization')
        route=c.load_json(b['routes']['text']);an=c.load_json(Path(a.run)/'02_analysis/analysis.json')
        prompt=c.read_prompt('storyboard.md')+'\nBRIEF:\n'+w.json_text(b)+'\nSOURCE EVIDENCE:\n'+w.json_text(an)+'\nNOTES:\n'+a.notes
        out=Path(a.run)/'03_storyboard'/('response-'+a.tag);out.mkdir(parents=True,exist_ok=False)
        sb=Client().analyze(prompt,[],route,out)
        c.log(a.run,step='storyboard',authorization=a.analysis_budget_authorization,response=str(out/'response.json'),cost=None)
    w.validate_storyboard(sb,b,meta);c.write_new(dest,sb);w.select_storyboard(a.run,dest)
    md=['# '+sb.get('title','Storyboard'),'','| Shot | Time | Function | Entry → action → exit | Keyframe |','|---|---|---|---|---|']
    for s in sb['shots']:md.append(f'| {s["id"]} | {s["start"]}–{s["end"]} | {s.get("function", "")} | {s["entry_state"]} → {s["action"]} → {s["exit_state"]} | {s["keyframe_brief"]} |')
    dest.with_suffix('.md').write_text('\n'.join(md),encoding='utf-8');print(dest)
if __name__=='__main__':main()
