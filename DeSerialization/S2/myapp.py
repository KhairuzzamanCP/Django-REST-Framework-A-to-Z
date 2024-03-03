
import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Rana',
    'roll': 1011,
    'number': '0199448484848',
    'city': 'Rangpur'
}
'''
# dumps(): এটি একটি ফাংশন যা একটি পাইথন অবজেক্ট নেয় এবং তাকে JSON ফরম্যাটে স্ট্রিং এ রূপান্তর করে।
# '''
json_data = json.dumps(data)
'''
# এই লাইনে, json.dumps(data) হলো ডাটা স্ট্রাঙ্গ এ রূপান্তরের প্রক্রিয়া, যে টাকে এরপরে নির্দিষ্ট কাজে ব্যবহার করা যেতে পারে, যেমন ডাটা নেটওয়ার্কে পাঠাতে বা ফাইলে লেখার জন্য।
# '''
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)



  
