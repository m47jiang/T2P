import json

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
    response = requests.get(url)
    return response.content

print grabfromdatabase("Lassie")