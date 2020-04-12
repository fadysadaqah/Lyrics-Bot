from __future__ import unicode_literals
import youtube_dl

def get_audio(video_id):
    file_path="audio/"+video_id+".m4a"
    ydl_opts = {
        'outtmpl': file_path,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',            
            'preferredquality':'320'
        }],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        video_url="https://www.youtube.com/watch?v="+str(video_id)
        ydl.download([video_url])