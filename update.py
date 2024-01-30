import requests
import json

URL = 'http://127.0.0.1:8000/bangla/desrlz/'

updatedata = {
    'student_id' : 101,
    'student_dept': 'Android',
    'student_age': 20
}

json_data = json.dumps(updatedata)
req = requests.put(url = URL, data = json_data)
data = req.json()
print(data)
