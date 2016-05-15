import json
import urllib2

import requests


def dumptodatabase(payload):
    req = requests.put("https://blinding-inferno-9101.firebaseio.com/bro.json", data=json.dumps(payload))

    print(req.content)

def grabfromdatabase(request):

    plantname = {"Beatrice":'Plant1',
                 "Lassie":'Plant2',
                 "Paul":'Plant3',
                 }
    url = 'https://blinding-inferno-9101.firebaseio.com/'+plantname[request]+'.json'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    answer = response.read().decode("utf-8")
    response.close()
    return answer

demoflower = {"name": "bob"}
flower = grabfromdatabase("Lassie")
newflower = eval(flower)
print newflower["humidity"]