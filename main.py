from cc_youtube import *
from audio_youtube import get_audio
from lyrics2 import *

video_id=input("Enter the Video id \n")
song_name=input("Enter the Song Name \n")
# video_id=u"8J9Vp48kJOA"
srt = get_cc(video_id)
try:
    create_video('img/bg.jpeg',video_id,srt,"Righteous",20,song_name)
except:
    get_audio(video_id)
    create_video('img/bg.jpeg',video_id,srt,"Righteous",20,song_name)