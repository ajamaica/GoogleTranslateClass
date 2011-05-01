from urllib import *
import json
key = "'Aca la llave'"
class google_translate:
    def __init__(self, key, f, t):
        self.key=key
        self.f=f
        self.t=t
        self.baseUrl="https://www.googleapis.com/language/translate/v2"
        

    def url(self, option):
        if option=="d":
            extra="/detect?"
        if option=="t":
            extra="?"
        if option=="l":
            extra="/languages?"
        return self.baseUrl+extra+"key="+self.key

    def translate(self, string):
        api = urlopen(self.url('t')+"&q="+string+"&source="+self.f+"&target="+self.t)
        return json.loads(api.read())['data']['translations'][0]['translatedText']
    
    def getLangs(self):
        api = urlopen(self.url('l')+'&target=en')
        jsonC = json.loads(api.read())['data']['languages']
        langs = []
        for i in jsonC:
            langs.append(i['name'])
        return langs
    
    def detectarLang(self, string):
        api = urlopen(self.url('d')+"&q="+string)
        return json.loads(api.read())['data']['detections'][0][0]['language']