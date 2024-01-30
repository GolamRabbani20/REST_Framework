import requests
import json

URL = 'http://127.0.0.1:8000/bangla/desrlz/'
data = {
    'student_id': 105,
}

#Python dict to json
json_data = json.dumps(data)
#print(json_data)
r = requests.delete(url = URL, data = json_data)
#print('r:', r)
data = r.json()
print(data)
