import googletrans
from googletrans import Translator
translator = Translator()

def translate(srt,froom,to):
    for i in srt:
        result = translator.translate(i["text"],dest=to,src=froom)
        print(result.text)
        i["text"]=result.text

