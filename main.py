from cc_youtube import *
from audio_youtube import get_audio
from lyrics2 import *
video_id=input("Enter the Video id \n")
# video_id=u"8J9Vp48kJOA"
get_audio(video_id)
srt = get_cc(video_id)
create_video('img/bg3.jpg',video_id,srt,"Righteous",60)
