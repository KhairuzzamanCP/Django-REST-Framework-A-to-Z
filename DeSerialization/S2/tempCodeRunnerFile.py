r = requests.post(url = URL, data= json_data)

data = r.json()
print(data)