from cc_youtube import *
from audio_youtube import get_audio
from lyrics2 import *
from random import randrange
from translate import translate
from cover import create_cover
def create_all(video_id,song_name,singer_name,font,image,fps,font_size):
    srt = get_cc(video_id)
    create_cover(image,font,song_name,singer_name,song_name)
    try:
        create_video(image,video_id,srt,font,fps,song_name,font_size)
    except:
        get_audio(video_id)
        create_video(image,video_id,srt,font,fps,song_name,font_size)

video_id=input("Enter the Video id \n")
song_name=input("Enter the Song Name \n")
artist_name=input("Enter the artist name \n")
img_id=input("Enter the image ID \n")
fps=input("Enter the fps \n")


create_all(video_id,song_name,artist_name,'Righteous',img_id,int(fps),90) 
    
