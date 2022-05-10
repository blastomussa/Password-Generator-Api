import requests

ROOT="http://127.0.0.1:5000/"

response = requests.get(ROOT + "generate")
#response = requests.get(ROOT, {"type": "UTF"})

print(response.json())
