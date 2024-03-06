import requests
import json

Url = 'http://127.0.0.1:8000/studentapi/'

# def get_data(id = None):
#     data ={}
#     if id is not None:
#         data = {'id':id}
#     json_data = json.dumps(data)
#     r = requests.get(url= Url, data= json_data)
#     data = r.json()
#     print(data)
# get_data()

def post_data():
    data = {
        'name':'Rana',
        'roll': 201,
        'city':'Rajsahi'
    }
    json_data = json.dumps(data)
    r = requests.post(url= Url, data= json_data)
    data = r.json()
    print(data)
post_data()


# def update_data():
#     data = {
#         'id':4,
#         'name':'Rakib',
#         'city':'Borisal'
#     }
#     json_data = json.dumps(data)
#     r = requests.put(url= Url, data= json_data)
#     data = r.json()
#     print(data)
# update_data()

# def delete_data():
#     data = {'id':5}
#     json_data = json.dumps(data)
#     r = requests.delete(url= Url, data= json_data)
#     data = r.json()
#     print(data)

# delete_data()


