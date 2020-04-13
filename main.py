from cc_youtube import *
from audio_youtube import get_audio
from lyrics2 import *
from random import randrange
from translate import translate

video_id=input("Enter the Video id \n")
song_name=input("Enter the Song Name \n")
srt = get_cc(video_id)
img="img/"+str(randrange(8)+2)+".jpg"
img="img/12.jpg"
# translate(srt,'en','fr')
try:
    create_video(img,video_id,srt,"Righteous",1,song_name,90)
except:
    get_audio(video_id)
    create_video(img,video_id,srt,"Righteous",1,song_name,90)
    
