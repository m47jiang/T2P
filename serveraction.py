import json
import urllib2
from ast import literal_eval

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


def textinfo(info):
    plant = literal_eval(info)

    url =  'https://api.tropo.com/1.0/sessions?action=create&token=5357576a466678524946497a6a755761724c6b6c4f687a444956467068426e5456745450796d5a7349426264'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    answer = response.read().decode("utf-8")
    response.close()
    return answer