import requests
import json

URL = "http://127.0.0.1:8000/create/1/"

data = { 'title': 'piyush_kumar', 'content': 'This is a simple blog about top 10 vpn'}
data = json.dumps(data)
r = requests.put(url = URL,data = data)
data = r.json()
print(data)