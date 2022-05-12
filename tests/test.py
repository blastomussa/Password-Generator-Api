import requests

ROOT="http://127.0.0.1:5000/"

#response = requests.get(ROOT + "generate?NUM_WORDS=3&MAX=30")
response = requests.get(ROOT + "?GIB=True")
#response = requests.get(ROOT, {"type": "UTF"})

print(response.json())
