def update_data():
    data = {
        'id':4,
        'name':'Rakib',
        'city':'Borisal'
    }
    json_data = json.dumps(data)
    r = requests.put(url= Url, data= json_data)
    data = r.json()
    print(data)
update_data()