# -*- coding: utf-8 -*-
"""Offline behavior tests. No network, credentials, model calls or historical run mutations."""
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import yaml
from PIL import Image
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import common as c
import workflow as w
from ark_cli import Client, CLIError, validate_job
from gen_images import do_pick
from edit import build as build_edit
from qa import audit

class FakeClient:
    def __init__(self,fail=False):self.calls=[];self.fail=fail
    def live_check(self,route):pass
    def generate(self,job,directory):
        self.calls.append(job['id'])
        if self.fail:raise CLIError('connection lost after possible submission')
        return {'task_id':'task-'+str(len(self.calls)),'status':'queued'}
    def get(self,task_id,route):return {'task_id':task_id,'status':'running','usage':{'completion_tokens':42}}

class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.run=self.root/'run';self.run.mkdir()
        self.image=self.root/'key.png';Image.new('RGB',(64,64),'orange').save(self.image)
        self.resource=self.root/'resource.json';c.write_new(self.resource,{'id':'ep-test','invocable':True})
        self.cap=self.root/'cap.json';c.write_new(self.cap,{'fixture':'offline'})
        self.route={'service':'volcengine','profile':'fixture','region':'cn-beijing','base_url':'https://example.invalid',
                    'resource':'ep-test','model':'fixture-model','model_version':'v1','modality':'video','transport':'inline-local',
                    'checked_at':c.now(),'constraints_reviewed':True,'input_roles':['first_frame','reference_image'],
                    'params':{'duration':{'support':True,'min':4,'max':30},'resolution':{'support':True,'enum':['480p','720p']},
                              'ratio':{'support':True,'enum':['16:9','9:16']},'generate_audio':{'support':True,'enum':[True,False]}},
                    'resource_evidence':c.file_ref(self.resource),'capability_evidence':c.file_ref(self.cap)}
        self.routefile=self.root/'route.json';c.write_new(self.routefile,self.route)
        self.brief={'mode':'creative','fidelity':'adaptation','text_policy':'none','audio':{'approach':'silent','generate_audio':False},
                    'cast':[{'id':'pet','references':[str(self.image)],'invariants':'Never mirror markings'}],
                    'output':{'duration':8,'ratio':'16:9','route':'plates','resolution':'720p','takes':1},
                    'routes':{'video':str(self.routefile)},'budget':{'cap':10,'currency':'USD','authorization':'user approved fixture budget','max_attempts_per_job':2}}
        self.briefpath=self.root/'brief.yaml';self.save_brief()
        self.sb={'title':'Fixture','duration':8,'shots':[self.shot('1',0,4),self.shot('2',4,8)]}
        self.sbfile=self.run/'03_storyboard/storyboard-v1.json';c.write_new(self.sbfile,self.sb);w.select_storyboard(self.run,self.sbfile)
        c.write_new(self.run/'01_probe/meta.json',{'duration':188,'ratio':'16:9','coverage':'sampled-observations'})
        c.write_new(self.run/'05_images/picks.json',{'keyframes':{'1':str(self.image),'2':str(self.image)}})
    def tearDown(self):self.tmp.cleanup()
    def shot(self,id,start,end):return {'id':id,'start':start,'end':end,'action':'walk forward','entry_state':'paws grounded','exit_state':'stop facing camera','keyframe_brief':'wide pet shot','cast':['pet'],'onscreen_text':''}
    def save_brief(self):self.briefpath.write_text(yaml.safe_dump(self.brief))
    def priced(self):
        jobs=w.build_jobs(self.run,c.load_brief(self.briefpath),'video')
        price={'checked_at':c.now(),'source':'offline fixture, not a real quote','currency':'USD','jobs':{j['id']:{'request_hash':j['request_hash'],'items':[{'quantity':4,'unit_quantity':1,'price':0.25,'unit':'second','charge_item':'fixture-output'}]} for j in jobs}}
        f=self.root/('prices-'+str(len(list(self.root.glob('prices*'))))+'.json');c.write_new(f,price)
        self.brief['pricing']=str(f);self.save_brief()
        return w.package(self.run,self.briefpath,'video')
    def confirm(self,pkg,ids=None):w.approve(self.run,pkg,ids or ['S-1','S-2'],'User confirmed the displayed fixture prompts and frames')
    def test_creative_no_product_and_review_files(self):
        pkg=self.priced();data=c.load_json(pkg)
        self.assertEqual(len(data['jobs']),2);self.assertTrue((pkg.parent/'review.html').exists());self.assertTrue((pkg.parent/'contact.jpg').exists())
        self.assertNotIn('Link in bio',data['jobs'][0]['prompt']);self.assertIn('Never mirror',data['jobs'][0]['prompt'])
    def test_no_approval_no_submission(self):
        pkg=self.priced();fake=FakeClient()
        with self.assertRaisesRegex(ValueError,'confirmation'):w.submit(self.run,pkg,['S-1'],fake)
        self.assertEqual(fake.calls,[]);self.assertEqual(w.tasks(self.run),[])
    def test_partial_approval(self):
        pkg=self.priced();self.confirm(pkg,['S-1']);fake=FakeClient()
        with self.assertRaises(ValueError):w.submit(self.run,pkg,['S-1','S-2'],fake)
        self.assertEqual(fake.calls,[])
        records=w.submit(self.run,pkg,['S-1'],fake)
        self.assertEqual(fake.calls,['S-1']);self.assertEqual(records[0]['task_id'],'task-1')
        self.assertEqual(w.tasks(self.run)[0]['task_id'],'task-1')
    def test_duplicate_submit_and_resume(self):
        pkg=self.priced();self.confirm(pkg);fake=FakeClient();records=w.submit(self.run,pkg,['S-1'],fake)
        with self.assertRaises(ValueError):w.submit(self.run,pkg,['S-1'],fake)
        r=w.resume(self.run,records[0]['id'],fake);self.assertEqual(r['status'],'running');self.assertEqual(fake.calls,['S-1'])
    def test_mutated_keyframe_blocks(self):
        pkg=self.priced();self.confirm(pkg);Image.new('RGB',(64,64),'blue').save(self.image)
        with self.assertRaises(ValueError):w.submit(self.run,pkg,['S-1'],FakeClient())
    def test_picks_changed_blocks(self):
        pkg=self.priced();self.confirm(pkg);other=self.root/'other.png';Image.new('RGB',(64,64),'blue').save(other)
        do_pick(self.run,['shot1='+str(other)])
        with self.assertRaises(ValueError):w.submit(self.run,pkg,['S-1'],FakeClient())
    def test_prompt_tampering_blocks(self):
        pkg=self.priced();self.confirm(pkg);d=c.load_json(pkg);d['jobs'][0]['prompt']='changed';c.save_json(pkg,d)
        with self.assertRaises(ValueError):w.submit(self.run,pkg,['S-1'],FakeClient())
    def test_settings_changes_require_review(self):
        for field,value in [('resolution','480p'),('duration',9)]:
            pkg=self.priced();self.confirm(pkg);old=self.brief['output'][field];self.brief['output'][field]=value;self.save_brief()
            with self.assertRaises(ValueError):w.submit(self.run,pkg,['S-1'],FakeClient())
            self.brief['output'][field]=old;self.save_brief()
    def test_audio_change_requires_review(self):
        pkg=self.priced();self.confirm(pkg);self.brief['audio']['generate_audio']=True;self.save_brief()
        with self.assertRaises(ValueError):w.submit(self.run,pkg,['S-1'],FakeClient())
    def test_unknown_price_not_zero(self):
        pkg=w.package(self.run,self.briefpath,'video');self.confirm(pkg)
        self.assertIsNone(c.load_json(pkg)['jobs'][0]['quote']['amount'])
        with self.assertRaisesRegex(ValueError,'Unknown price'):w.submit(self.run,pkg,['S-1'],FakeClient())
    def test_budget_reserves_and_batch(self):
        self.brief['budget']['cap']=1.5;self.save_brief();pkg=self.priced();self.confirm(pkg);fake=FakeClient()
        with self.assertRaisesRegex(ValueError,'cap exceeded'):w.submit(self.run,pkg,['S-1','S-2'],fake)
        self.assertFalse(fake.calls)
        w.submit(self.run,pkg,['S-1'],fake)
        with self.assertRaisesRegex(ValueError,'cap exceeded'):w.submit(self.run,pkg,['S-2'],fake)
    def test_ambiguous_create_stops_batch(self):
        pkg=self.priced();self.confirm(pkg);fake=FakeClient(fail=True)
        with self.assertRaises(CLIError):w.submit(self.run,pkg,['S-1','S-2'],fake)
        self.assertEqual(fake.calls,['S-1']);self.assertEqual(w.tasks(self.run)[0]['status'],'submission-unknown')
        with self.assertRaisesRegex(ValueError,'Unreconciled'):w.submit(self.run,pkg,['S-2'],FakeClient())
    def test_storyboard_not_selected_by_mtime(self):
        other=self.run/'03_storyboard/storyboard-z.json';c.write_new(other,{'invalid':True})
        self.assertEqual(w.selected_storyboard(self.run),str(self.sbfile.resolve()))
    def test_sampled_source_cannot_close_match(self):
        self.brief['fidelity']='close-timing';self.save_brief()
        with self.assertRaisesRegex(ValueError,'measured source'):w.build_jobs(self.run,c.load_brief(self.briefpath),'video')
    def test_missing_text_choice_blocks_production_not_loading(self):
        self.brief['text_policy']=None;self.save_brief();c.load_brief(self.briefpath)
        with self.assertRaisesRegex(ValueError,'text_policy'):w.build_jobs(self.run,c.load_brief(self.briefpath),'video')
    def test_unsupported_parameter_and_service(self):
        self.route['service']='byteplus';c.save_json(self.routefile,self.route)
        with self.assertRaisesRegex(ValueError,'BytePlus'):w.build_jobs(self.run,c.load_brief(self.briefpath),'video')
        self.route['service']='volcengine';self.route['params']['resolution']['enum']=['480p'];c.save_json(self.routefile,self.route)
        with self.assertRaisesRegex(ValueError,'Unsupported resolution'):w.build_jobs(self.run,c.load_brief(self.briefpath),'video')
    def test_ad_brief_still_supported(self):
        self.brief.pop('mode');self.brief['product']={'name':'bottle','images':[str(self.image)],'geometry':'One nozzle','selling_points':['foldable']}
        self.brief['text_policy']='post';self.sb['shots'][0]['onscreen_text']='Fold it';c.save_json(self.sbfile,self.sb);w.select_storyboard(self.run,self.sbfile);self.save_brief()
        jobs=w.build_jobs(self.run,c.load_brief(self.briefpath),'video')
        self.assertEqual(jobs[0]['mode'],'ad');self.assertNotIn('On-screen text exactly',jobs[0]['prompt']);self.assertIn('One nozzle',jobs[0]['prompt'])
    def test_transition_reference_required(self):
        self.sb['shots'][1]['keyframe_states']={'bloom':{'entry_state':'closed bud','action':'open petals','exit_state':'open flower','keyframe_brief':'same grass patch'}}
        c.save_json(self.sbfile,self.sb);w.select_storyboard(self.run,self.sbfile)
        with self.assertRaisesRegex(ValueError,'transition frame'):w.build_jobs(self.run,c.load_brief(self.briefpath),'video')
        do_pick(self.run,['bloom='+str(self.image)]);jobs=w.build_jobs(self.run,c.load_brief(self.briefpath),'video')
        self.assertTrue(any(r['label']=='Transition state bloom' for r in jobs[1]['references']))
    def test_stale_price_rejected(self):
        pkg=self.priced();price=c.load_json(self.brief['pricing']);price['jobs']['S-1']['request_hash']='old';c.save_json(self.brief['pricing'],price)
        pkg=w.package(self.run,self.briefpath,'video');self.confirm(pkg)
        with self.assertRaisesRegex(ValueError,'Unknown price'):w.submit(self.run,pkg,['S-1'],FakeClient())
    def test_batch_tampering_cannot_expand_approval(self):
        pkg=self.priced();self.confirm(pkg);d=c.load_json(pkg);d['takes']=2;c.save_json(pkg,d)
        with self.assertRaises(ValueError):w.submit(self.run,pkg,['S-1'],FakeClient())
    def test_image_generation_not_video_approval(self):
        image_route=copy.deepcopy(self.route);image_route['modality']='image';image_route['params']={};p=self.root/'image-route.json';c.write_new(p,image_route)
        self.brief['routes']['image']=str(p);self.save_brief()
        image_pkg=w.package(self.run,self.briefpath,'image');w.approve(self.run,image_pkg,['KF-1'],'User authorized image budget and reference upload')
        video_pkg=self.priced()
        with self.assertRaisesRegex(ValueError,'confirmation'):w.submit(self.run,video_pkg,['S-1'],FakeClient())
    def test_unaffected_shot_keeps_approval_after_repair(self):
        pkg=self.priced();self.confirm(pkg,['S-1'])
        repaired=copy.deepcopy(self.sb);repaired['shots'][1]['action']='turn toward the other pet'
        v2=self.run/'03_storyboard/storyboard-v2.json';c.write_new(v2,repaired);w.select_storyboard(self.run,v2)
        # Retain the old quote exactly for the unaffected shot; add a new quote only for the repair.
        jobs=w.build_jobs(self.run,c.load_brief(self.briefpath),'video');price=c.load_json(self.brief['pricing'])
        price['jobs']['S-2']['request_hash']=jobs[1]['request_hash'];newprice=self.root/'repair-prices.json';c.write_new(newprice,price)
        self.brief['pricing']=str(newprice);self.save_brief();newpkg=w.package(self.run,self.briefpath,'video')
        self.assertTrue(w.approved(self.run,c.load_json(newpkg)['jobs'][0]))
        self.assertFalse(w.approved(self.run,c.load_json(newpkg)['jobs'][1]))
        w.submit(self.run,newpkg,['S-1'],FakeClient())
    def test_download_pending_does_not_resubmit(self):
        class Completed(FakeClient):
            def get(self,task_id,route):return {'task_id':task_id,'status':'succeeded'}
        pkg=self.priced();self.confirm(pkg);fake=Completed();r=w.submit(self.run,pkg,['S-1'],fake)[0]
        r=w.resume(self.run,r['id'],fake);self.assertEqual(r['status'],'download-pending')
        with self.assertRaises(ValueError):w.submit(self.run,pkg,['S-1'],fake)
        self.assertEqual(fake.calls,['S-1'])
    def test_successful_image_is_frozen_locally(self):
        record={'modality':'image','status':'succeeded','output_dir':str(self.root/'frozen')}
        Path(record['output_dir']).mkdir()
        w.update_result(record,{'status':'succeeded','local_path':str(self.image)})
        self.assertNotEqual(record['file']['path'],str(self.image));c.verify_file(record['file'])
    def test_fractional_edit_can_use_longer_plate(self):
        sb=copy.deepcopy(self.sb);sb['shots'][0]['end']=3.8;sb['shots'][1]['start']=3.8
        sb['shots'][0]['generation_duration']=4;sb['shots'][1]['generation_duration']=5
        f=self.run/'03_storyboard/storyboard-fractional.json';c.write_new(f,sb);w.select_storyboard(self.run,f)
        jobs=w.build_jobs(self.run,c.load_brief(self.briefpath),'video');self.assertEqual([j['settings']['duration'] for j in jobs],[4,5])
    def test_external_expenses_count_toward_cap(self):
        self.brief['budget']['external_reserve']=9.5;self.save_brief();pkg=self.priced();self.confirm(pkg)
        with self.assertRaisesRegex(ValueError,'cap exceeded'):w.submit(self.run,pkg,['S-1'],FakeClient())
    def test_reference_service_model_change_blocks(self):
        pkg=self.priced();self.confirm(pkg);self.route['model']='different-model';c.save_json(self.routefile,self.route)
        with self.assertRaises(ValueError):w.submit(self.run,pkg,['S-1'],FakeClient())
    def test_job_attempt_cap_blocks_multi_take(self):
        self.brief['output']['takes']=3;self.save_brief();pkg=self.priced();self.confirm(pkg)
        with self.assertRaisesRegex(ValueError,'allowance'):w.submit(self.run,pkg,['S-1'],FakeClient())
    def test_foreign_run_cannot_reset_budget(self):
        pkg=self.priced();self.confirm(pkg);other=self.root/'other-run';other.mkdir()
        with self.assertRaisesRegex(ValueError,'another run'):w.submit(other,pkg,['S-1'],FakeClient())
    def test_cli_arguments_no_shell_and_caller_metadata(self):
        job=w.build_jobs(self.run,c.load_brief(self.briefpath),'video')[0];calls=[]
        def runner(args,**kw):
            calls.append((args,kw));text='1.2.0' if args==['ve','version'] else json.dumps({'task_id':'real-shape','status':'queued'})
            return subprocess.CompletedProcess(args,0,text,'')
        client=Client(runner);client.live_check=lambda _:None
        with patch.dict(os.environ,{'VE_CALLER_NAME':'codex','VE_SKILL_NAME':'volcengine-cli','ARKCLI_CALLER_NAME':'bad'}):
            result=client.generate(job,self.root)
        args,kw=calls[-1];self.assertEqual(result['task_id'],'real-shape');self.assertIn('--generate-audio=false',args)
        self.assertIn('first_frame:@'+str(self.image.resolve()),args);self.assertNotIn('ARKCLI_CALLER_NAME',kw['env']);self.assertFalse(kw.get('shell',False))
    def test_route_drift_stops_before_create(self):
        client=Client();client.query=lambda *a,**kw:{'id':'ep-different','invocable':True}
        with self.assertRaisesRegex(CLIError,'changed'):client.live_check(self.route)

class MediaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory();cls.root=Path(cls.tmp.name);cls.video=cls.root/'fixture.mp4'
        subprocess.run(['ffmpeg','-v','error','-f','lavfi','-i','color=c=red:s=160x90:r=24','-t','1','-c:v','libx264','-pix_fmt','yuv420p',str(cls.video)],check=True)
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def test_technical_success_not_semantic_pass(self):
        result=audit(self.video,{'duration':1,'dimensions':[160,90],'fps':24,'audio_required':False})
        self.assertTrue(all(result['technical_checks'].values()));self.assertEqual(result['status'],'review-incomplete')
    def test_wrong_review_hash_rejected(self):
        with self.assertRaises(ValueError):audit(self.video,{'duration':1,'dimensions':[160,90],'fps':24},{'file_sha256':'wrong'})
    def test_edit_out_of_range_rejected(self):
        run=self.root/'edit-run';sb={'duration':1,'shots':[{'id':'1','start':0,'end':1}]};f=run/'sb.json';c.save_json(f,sb);w.select_storyboard(run,f)
        selection={'shots':{'1':{'file':str(self.video),'reuse_authorization':'fixture','provenance':'generated fixture','qa':'approved','source_in':0.5}},'text_policy':'none','output':{}}
        with self.assertRaisesRegex(ValueError,'range'):build_edit(run,selection,self.root/'edit.json')

if __name__=='__main__':unittest.main()
