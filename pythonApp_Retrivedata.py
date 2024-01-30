import requests

URL = 'http://127.0.0.1:8000/bangla/stinfo/'

res = requests.get(url=URL)

data = res.json()
print(data)