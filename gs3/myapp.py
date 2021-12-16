# This is a a python program which uses django rest framework API for CRUD operations 
import requests, json

URL = "http://127.0.0.1:8000/studentapi/"

# the data is hardcoded for now

def get_data(id = None):
    # retreive data acording to id
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

get_data()

def post_data():
    data = {
        'name' : 'Ravi',
        'roll' : 104,
        'city' : 'Dhanbad'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

# post_data()
def update_data():
    data = {
        'id' : 13,
        'name' : 'manish',
        'city' : 'ranchi' 
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# update_data()
def delete_data():
    data = {'id': 3}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

# delete_data()

