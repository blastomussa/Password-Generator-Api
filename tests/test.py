import requests

ROOT="http://127.0.0.1:5000/"

response = requests.get(ROOT + "/api/v1")
#response = requests.get(ROOT + "?GIB=True")
#response = requests.get(ROOT, {"type": "UTF"})

print(response.json())
