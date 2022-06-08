# test: python3 unit-test.py && echo 'success'
import requests
import sys

URL="http://127.0.0.1:5000/api/v1"

response = requests.get(URL)

if response.status_code != 200:
    sys.exit(1)

response = response.json()

if 'password' not in response.keys():
    sys.exit(1)
