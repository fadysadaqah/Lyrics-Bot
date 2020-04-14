import os
def create_cover(img,font,name,singer,output):
    output = output.replace(' ','_')
    os.system("""
    convert 'img/{}.jpg' \
    -family {} \
    -pointsize 185 \
    -gravity center \
    -fill '#333333aa' \
    -annotate +10-39 '{}' \
    'img/{}.jpg'""".format(img,font,name,output))

    os.system("""
    convert 'img/{}.jpg' \
    -family {} \
    -pointsize 185 \
    -gravity center \
    -fill '#ffffff' \
    -annotate +0-50 '{}' \
    'img/{}.jpg'""".format(output,font,name,output))

    os.system("""
    convert 'img/{}.jpg' \
    -family {} \
    -pointsize 85 \
    -gravity center \
    -fill '#333333aa' \
    -annotate +5+110 '{}' \
    'img/{}.jpg'""".format(output,font,singer,output))

    os.system("""
    convert 'img/{}.jpg' \
    -family {} \
    -pointsize 85 \
    -gravity center \
    -fill '#ffffff' \
    -annotate +0+105 '{}' \
    'img/{}.jpg'""".format(output,font,singer,output))
create_cover('6','Changa','name','شيرين','ds ff')
