from urllib.request import Request, urlopen
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
while(True):
    key = input("temp(q for decrease, w for increase), humidity(e for decrease, r for increase) ")
    if key == 'w':
        temperature=temperature+1
    elif key == 'q':
        temperature=temperature-1
    elif key == 'e':
        humidity = humidity - 1
    elif key == 'r':
        humidity = humidity + 1
    setValue(temperature, humidity)