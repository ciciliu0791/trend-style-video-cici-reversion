#!/usr/bin/env python3
"""Build a validated, versioned edit manifest for HyperFrames. Never edits source media."""
import argparse
from pathlib import Path
import common as c
import workflow as w

def build(run,selection,output):
    sb=c.load_json(w.selected_storyboard(run));selected=selection['shots']; clips=[]
    if set(selected)!=set(str(s['id']) for s in sb['shots']):raise ValueError('Select exactly every storyboard shot')
    for s in sb['shots']:
        pick=selected[str(s['id'])]
        if pick.get('task_record'):
            task=c.load_json(Path(run)/'tasks'/(pick['task_record']+'.json'))
            if task['status']!='succeeded' or not task.get('file'):raise ValueError('Task has no verified local output')
            ref=task['file'];c.verify_file(ref);provenance={'task_id':task.get('task_id'),'record_id':task['id']}
        else:
            if not pick.get('reuse_authorization') or not pick.get('provenance'):raise ValueError('Reused footage needs authorization and provenance')
            ref=c.file_ref(pick['file']);provenance=pick['provenance']
        meta=c.ffprobe(ref['path']);start=float(pick.get('source_in',0));duration=s['end']-s['start']
        if start<0 or start+duration>meta['duration']+0.001:raise ValueError(f'Source range outside shot {s["id"]}')
        if pick.get('qa')!='approved':raise ValueError('Selected motion must pass shot-level review')
        clips.append({'shot_id':str(s['id']),'file':ref,'source_in':start,'used_duration':duration,'timeline_start':s['start'],
                      'timeline_end':s['end'],'source_dimensions':[meta['width'],meta['height']],'provenance':provenance,
                      'text':s.get('onscreen_text',''),'dialogue':c.dialogue_lines(s)})
    cues=selection.get('audio_cues',[])
    for cue in cues:
        cue['file']=c.file_ref(cue['path'])
        if not 0<=cue['start']<cue['end']<=sb['duration']:raise ValueError('Audio cue outside timeline')
    result={'schema_version':2,'storyboard':w.manifest(run)['storyboard'],'duration':sb['duration'],'clips':clips,'audio_cues':cues,
            'text_policy':selection['text_policy'],'output':selection['output'],'status':'ready-for-HyperFrames','rendered_file':None}
    if result['text_policy'] not in ('generated','post','none'):raise ValueError('Resolve text policy')
    c.write_new(output,result);return result

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run',required=True);p.add_argument('--selection',required=True);p.add_argument('--output',required=True)
    a=p.parse_args();build(a.run,c.load_json(a.selection),a.output);print(a.output)
if __name__=='__main__':main()
