from moviepy.editor import *

# img = ['img/bg.jpg']
# # clips = ImageClip(img[0]).set_duration(30)

# clips = [ImageClip(m).set_duration(2)
#       for m in img]

# concat_clip = concatenate_videoclips(clips, method="compose")
# concat_clip.write_videofile("test.mp4", fps=24,audio="test.mp3")

#####################################################
text_list = ["Piggy", "Kermit", "Gonzo", "Fozzie"]
clip_list = []

for text in text_list:
    txt_clip = TextClip(text, fontsize = 10, color = 'white').set_duration(30)
    clip_list.append(txt_clip)
print(txt_clip) 

final_clip = concatenate(clip_list, method = "compose")
final_clip.write_videofile("my_concatenation.mp4", fps = 24, codec = 'mpeg4',audio="test.mp3")