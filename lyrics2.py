from moviepy.editor import *
def create_text_clip(srt,font):
    clip_list=[]
    old_start=0
    old_duration=0
    for i in srt :
        item_duration = i["duration"]
        item_start = i["start"]
        if item_start-old_start != old_duration:
            space_duration = item_start-old_start-old_duration
            txt_clip = TextClip (" ", fontsize=70, color='white' ,align="center").set_duration(t=space_duration)
            clip_list.append(txt_clip)      
        txt_clip = TextClip(i["text"].encode('utf8'),font=font, fontsize=70, color='white' ,align="center").set_duration(t=item_duration)
        clip_list.append(txt_clip)
        old_start=item_start
        old_duration=item_duration
    final_clip = concatenate(clip_list, method = "compose").set_pos("center")
    return final_clip

def create_video(background,video_id,srt,font,fps):
    audio_file = "audio/"+video_id+'.mp3'
    video_name=video_id+".mp4"
    audio_time = AudioFileClip(audio_file).duration
    clips = [ImageClip(background).set_duration(audio_time)]
    clip = concatenate_videoclips(clips, method="compose")
    clip = CompositeVideoClip([clip, create_text_clip(srt,font)])
    clip.write_videofile(video_name,fps=fps,audio=audio_file)