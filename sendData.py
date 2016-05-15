from urllib.request import Request, urlopen
import getch
import requests
import json

def setValue(temperature, humidity):
    payload = {"Plant1": {"name": "Lassie",
                          "temp": temperature,
                          "humid": humidity,
                          }}
    req = requests.put("https://blinding-inferno-9101.firebaseio.com/bro.json", data=json.dumps(payload))
    print(req.content)

temperature = 20
humidity = 60
while():
    key = ord(getch())
    if key == 72:
        temperature=temperature+1;
    elif key == 80:
        temperature=temperature-1;
    setValue(temperature, humidity)