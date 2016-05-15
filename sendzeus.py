import json
import random
import urllib.request
from ast import literal_eval
import requests
from zeus import client

def grabfromdatabase():
    url = 'https://blinding-inferno-9101.firebaseio.com/.json'
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    answer = response.read().decode("utf-8")
    response.close()
    return answer


payload = grabfromdatabase()
z = client.ZeusClient('70f85e2c', payload)
z.sendMetric("plants",payload)