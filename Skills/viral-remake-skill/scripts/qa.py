#!/usr/bin/env python3
"""Technical delivery checks plus separately evidenced semantic review.
No implicit VLM/ASR calls. Optional model second opinions use analyze.py and a new authorized run.
"""
import argparse
from pathlib import Path
import subprocess
import common as c

def audit(video,expected,review=None):
    meta=c.ffprobe(video)
    decode=subprocess.run(['ffmpeg','-v','error','-i',str(video),'-f','null','-'],capture_output=True,text=True)
    black=subprocess.run(['ffmpeg','-v','info','-i',str(video),'-vf','blackdetect=d=0.1:pix_th=0.10','-an','-f','null','-'],capture_output=True,text=True)
    import re
    candidates=re.findall(r'black_start:[^\n]+',black.stderr)
    checks={'black_scan':black.returncode==0,'decode':decode.returncode==0,'duration':abs(meta['duration']-float(expected['duration']))<=1/max(meta['fps'],1)+0.001,
            'dimensions':[meta['width'],meta['height']]==expected['dimensions'],'fps':abs(meta['fps']-expected['fps'])<0.01,
            'audio':meta['has_audio'] if expected.get('audio_required') else True}
    semantic={k:{'status':'unverified','evidence':[]} for k in ('sampled_visual','motion_playback','transcription','direct_listening','final_frame','black_frame_review')}
    ref=c.file_ref(video)
    if review:
        if review.get('file_sha256')!=ref['sha256']:raise ValueError('Review belongs to a different delivered file')
        for k,v in review.get('checks',{}).items():
            if k not in semantic:raise ValueError('Unknown review dimension: '+k)
            if v.get('status') not in ('pass','failed','unverified','not-applicable'):raise ValueError('Invalid review status')
            if v['status']!='unverified' and not v.get('evidence'):raise ValueError('Review result requires evidence or N/A reason')
            semantic[k]=v
    required=['sampled_visual','motion_playback','final_frame']
    if expected.get('audio_required'):required.append('direct_listening')
    if expected.get('speech_required'):required.append('transcription')
    if candidates:required.append('black_frame_review')
    failed=not all(checks.values()) or any(v['status']=='failed' for v in semantic.values())
    unverified=any(semantic[k]['status']!='pass' for k in required)
    return {'file':ref,'metadata':meta,'technical_checks':checks,'black_frame_candidates':candidates,'review':semantic,
            'status':'needs-repair' if failed else 'review-incomplete' if unverified else 'reviewed-final',
            'limits':'Sampled evidence does not prove every transient frame; technical audio presence does not establish listening quality.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--video',required=True);p.add_argument('--expected',required=True)
    p.add_argument('--review');p.add_argument('--output',required=True)
    p.add_argument('--model-review-route',help='Optional verified text route for ONE paid second opinion')
    p.add_argument('--analysis-budget-authorization');a=p.parse_args()
    result=audit(a.video,c.load_json(a.expected),c.load_json(a.review) if a.review else None)
    if a.model_review_route:
        if not a.analysis_budget_authorization:p.error('Model review requires explicit --analysis-budget-authorization and reserved external budget')
        from ark_cli import Client
        directory=Path(a.output).with_suffix('.model-review');directory.mkdir(parents=True,exist_ok=False)
        prompt=c.read_prompt('qa.md')+'\nDELIVERED FILE: '+str(Path(a.video).resolve())+'\nSHA256: '+result['file']['sha256']+'\nEXPECTED: '+__import__('json').dumps(c.load_json(a.expected))
        opinion=Client().analyze(prompt,[a.video],c.load_json(a.model_review_route),directory)
        result['model_second_opinion']={'findings':opinion,'response':str(directory/'response.json'),'authorization':a.analysis_budget_authorization,
                                        'limits':'Second opinion only; does not automatically pass playback, transcript or listening checks.'}
    c.write_new(a.output,result);print(a.output,result['status'])
if __name__=='__main__':main()
