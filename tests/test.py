import requests

ROOT="http://127.0.0.1:5000/"

response = requests.get(ROOT+"hello")
print(response.json())
