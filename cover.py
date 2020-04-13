import os
os.system("""
convert img/13.jpg \
-family Righteous \
-pointsize 185 \
-gravity center \
-fill '#333333aa' \
-annotate +10-39 'Level of Concern' \
img/temp2.jpg""")

os.system("""
convert img/temp2.jpg \
-family Righteous \
-pointsize 185 \
-gravity center \
-fill '#ffffff' \
-annotate +0-50 'Level of Concern' \
img/temp2.jpg""")

os.system("""
convert img/temp2.jpg \
-family Righteous \
-pointsize 85 \
-gravity center \
-fill '#333333aa' \
-annotate +5+110 'Twenty One Pilots' \
img/temp2.jpg""")

os.system("""
convert img/temp2.jpg \
-family Righteous \
-pointsize 85 \
-gravity center \
-fill '#ffffff' \
-annotate +0+105 'Twenty One Pilots' \
img/temp2.jpg""")
# print(res)