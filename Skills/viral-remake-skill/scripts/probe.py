#!/usr/bin/env python3
"""Offline source probing and timestamped observation import. ASR is an explicit external stage."""
import argparse, json, os, re, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as c
from pathlib import Path



def ff(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def detect_cuts(path, threshold):
    out = subprocess.run(["ffmpeg", "-v", "info", "-i", path, "-an", "-vf",
                          f"scdet=threshold={threshold}:sc_pass=1,metadata=print:file=-", "-f", "null", "-"],
                         capture_output=True, text=True).stdout
    return sorted({round(float(t), 2) for t in re.findall(r"lavfi\.scd\.time=([\d.]+)", out)})


def shots_from_cuts(cuts, duration, min_len=0.4):
    bounds = [0.0]
    for t in cuts:
        if t - bounds[-1] >= min_len and duration - t >= min_len:
            bounds.append(t)
    bounds.append(duration)
    return [{"id": i + 1, "start": bounds[i], "end": bounds[i + 1]} for i in range(len(bounds) - 1)]


def scale_filter(meta, short=720):
    w, h = meta["width"], meta["height"]
    if min(w, h) <= short:
        return "scale=trunc(iw/2)*2:trunc(ih/2)*2"
    return f"scale=-2:{short}" if w > h else f"scale={short}:-2"


def contact_sheet(paths, out, labels=None, tile=300, cols=6):
    from PIL import Image, ImageDraw
    ims = [Image.open(p).convert("RGB") for p in paths]
    for im in ims:
        im.thumbnail((tile, tile))
    th = max(im.size[1] for im in ims) + 22
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (min(cols, len(ims)) * tile, rows * th), "white")
    d = ImageDraw.Draw(sheet)
    for i, im in enumerate(ims):
        x, y = (i % cols) * tile, (i // cols) * th
        sheet.paste(im, (x + (tile - im.size[0]) // 2, y))
        d.text((x + 4, y + th - 18), (labels or [os.path.basename(p) for p in paths])[i], fill="black")
    sheet.save(out, quality=88)
    return out


def main():
    ap=argparse.ArgumentParser(description="Offline source ingest; no transcription requests")
    ap.add_argument('--run',required=True)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--video');group.add_argument('--observations',help='JSON: URL, duration_seconds, observations [{time,evidence}], limits')
    ap.add_argument('--transcript',help='Externally verified transcript JSON with available and lines')
    ap.add_argument('--scdet',type=float,default=10.0)
    ap.add_argument('--cuts-reviewed',action='store_true',help='Only after inspecting detected cuts; enables close-timing use')
    a=ap.parse_args();d=Path(c.step_dir(a.run,'01_probe'));c.no_overwrite(d/'meta.json')
    transcript=c.load_json(a.transcript) if a.transcript else {'available':False,'lines':[],'reason':'Not transcribed; audio content unknown'}
    if a.observations:
        obs=c.load_json(a.observations)
        if not obs.get('url') or not obs.get('observations') or not obs.get('limits'):raise ValueError('Observations need URL, timestamped evidence and limitations')
        for item in obs['observations']:
            if not isinstance(item.get('time'),(int,float)) or not item.get('evidence'):raise ValueError('Each observation needs numeric time and evidence')
        c.write_new(d/'observations.json',obs)
        meta={'coverage':'sampled-observations','source_url':obs['url'],'duration':obs.get('duration_seconds'),'ratio':None,'analysis_video':None,'limits':obs['limits']}
        c.write_new(d/'shots.json',{'shots':[],'cuts':[],'coverage':'sampled-observations'})
    else:
        src=d/('source'+Path(a.video).suffix);c.no_overwrite(src);shutil.copy(a.video,src)
        meta=c.ffprobe(src);meta['ratio']=c.ratio_label(meta['width'],meta['height'])
        cuts=detect_cuts(str(src),a.scdet);shots=shots_from_cuts(cuts,meta['duration'])
        meta['coverage']='measured-cuts' if a.cuts_reviewed else 'detected-cuts-unreviewed'
        meta['measured_shots']=[dict(s) for s in shots] if a.cuts_reviewed else []
        meta['source']=c.file_ref(src);meta['analysis_video']=str((d/'analysis.mp4').resolve())
        ff('-i',str(src),'-vf',scale_filter(meta),'-c:v','libx264','-crf','28','-preset','veryfast','-an',meta['analysis_video'])
        meta['ref_video']=str(src.resolve()) # actual capability limits checked before submission, never truncate silently
        fdir=Path(c.step_dir(d,'frames'));frames=[]
        for s in shots:
            path=fdir/('shot'+str(s['id'])+'.jpg');ff('-ss',str((s['start']+s['end'])/2),'-i',str(src),'-frames:v','1','-q:v','3',str(path))
            s['frame']=str(path.resolve());frames.append(str(path))
        contact_sheet(frames,str(fdir/'contact.jpg'),[str(s['id']) for s in shots])
        c.write_new(d/'shots.json',{'shots':shots,'cuts':cuts,'threshold':a.scdet})
        if not meta['has_audio'] and not a.transcript:transcript={'available':True,'lines':[],'reason':'Source has no audio stream'}
    c.write_new(d/'transcript.json',transcript);c.write_new(d/'meta.json',meta)
    print(d/'meta.json')

if __name__=='__main__':main()
