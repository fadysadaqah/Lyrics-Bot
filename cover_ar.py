import os
def create_cover(img,font,name,singer,output):

    os.system("""
    convert 'img/{}.jpg' \
    -font {} \
    -gravity center \
    -fill '#000000' \
    -pointsize 185 pango:"{}" img/{}.jpg""".format(img,font,name,output))
create_cover('6','Changa','شيرين','ss','x')
