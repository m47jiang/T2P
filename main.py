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

    url = 'https://api.tropo.com/1.0/sessions?action=create&token=44526456527750486b54506d44496c464574584f4a4b6350627844584c4b5949436a47474c757a4768616458&numberToDial=4034799807&plantname=' + plant["name"] + '&hum=' + raw_input(plant["humidity"]) + '&temp=' + raw_input(plant["temperature"])
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    answer = response.read().decode("utf-8")
    response.close()
    if(answer=="success=true&token=44526456527750486b54506d44496c464574584f4a4b6350627844584c4b5949436a47474c757a4768616458&id=773dad4e3383070d4ed26c210e7bab9a"):
        return True
    else:
        return False

plant = grabfromdatabase("Beatrice")
print(textinfo(plant))