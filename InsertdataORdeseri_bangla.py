import requests
import json

URL = 'http://127.0.0.1:8000/bangla/desrlz/'

data = {
    "student_name":"Lata",
    "student_id":701,
    "student_dept":"MBA",
    "student_phn":"017553256",
    "student_age":25,
    "student_sex":"Female"
}

json_data = json.dumps(data)
req = requests.post(url = URL, data =  json_data)
data = req.json()
print(data)