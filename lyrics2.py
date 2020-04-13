from moviepy.editor import *
import re
def create_text_clip(srt,font,song_name,fontsize):
    clip_list=[]
    old_start=srt[0]["start"]
    old_duration=0
    txt_clip = TextClip(song_name.capitalize().encode('utf8'),font=font, fontsize=120, color='white' ,align="center").set_duration(srt[0]["start"])
    clip_list.append(txt_clip)
    for x in range(0,len(srt)):
        i=srt[x]
        item_duration = i["duration"]
        item_start = i["start"]
        if item_start-old_start != old_duration:
            space_duration = item_start-old_start-old_duration
            txt_clip = TextClip (" ", fontsize=70, color='white' ,align="center").set_duration(t=space_duration)
            clip_list.append(txt_clip)    
        if x != (len(srt)-1):
            if (i["duration"]+i["start"])>(srt[x+1]["start"]) or (i["duration"]+i["start"])==(srt[x+1]["start"]):
                item_duration=srt[x+1]["start"]-i["start"]
        txt_clip = TextClip(srt_filter(i["text"]).encode('utf8'),method="caption",font=font,size=(1800,1080), fontsize=fontsize, color='white' ,align="center").set_duration(t=item_duration)
        clip_list.append(txt_clip)
        old_start=item_start
        old_duration=item_duration
    final_clip = concatenate(clip_list, method = "compose").set_pos("center")
    return final_clip

def create_video(background,video_id,srt,font,fps,song_name,fontsize):
    audio_file = "audio/"+video_id+'.mp3'
    audio_time = AudioFileClip(audio_file).duration
    video_name=song_name+".mp4"
    clips = [ImageClip(background).set_duration(audio_time)]
    clip = concatenate_videoclips(clips, method="compose")
    clip = CompositeVideoClip([clip, create_text_clip(srt,font,song_name,fontsize)])
    clip.write_videofile(video_name,fps=fps,audio=audio_file,threads=10)

def srt_filter(srt):
    srt= srt.replace("♪ ","").replace(" ♪","").replace("♪","")
    return re.sub(r'^(?![\s\S])'," ",srt)