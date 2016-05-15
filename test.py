from urllib.request import Request, urlopen
import json
import requests
uri = 'https://api.relayr.io/devices/408af2ba-b838-4a73-b9f3-308979a5c6bb/readings'

def get_content(uri):
	req = Request(uri)
	req.add_header('Authorization', 'Bearer h2kFXSGsd14mSUTMeldk8jsoNArhGdEZ')
	req.add_header('Content-Type', 'application/json')
	response = urlopen(req)
	responseString = response.read().decode("utf-8")
	response.close()
	return responseString

jsonObject = json.loads(get_content(uri))

def setValue(temperature, humidity):
	payload = {"Plant1": {"name": "Lassie",
                          "temperature": temperature,
                          "humidity": humidity,
						  "light": 74,
                          },
			   "Plant2": {"name": "Elsa",
						  "temperature": 17,
						  "humidity": 45,
						  "light": 75,
						  },
			   "Plant3": {"name": "Napoleon",
						  "temperature": 19,
						  "humidity": 55,
						  "light": 73,
						  },
			   "numPlants": 3}
	req = requests.put("https://blinding-inferno-9101.firebaseio.com/.json", data=json.dumps(payload))

temperature = jsonObject["readings"][0]["value"]
humidity = jsonObject["readings"][1]["value"]
setValue(temperature, humidity)

