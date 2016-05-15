import requests
import json
payload = {"naming": "robert"}
req = requests.put("https://blinding-inferno-9101.firebaseio.com/bro.json", data=json.dumps(payload))
print(req.content)