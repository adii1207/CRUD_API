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
    headers = {'content-Type' : 'application/json'}
    r = requests.get(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)

# get_data(2)

def post_data():
    data = {
        'name' : 'Parikshit',
        'roll' : 4,
        'city' : 'Bilaspur'
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)

# post_data()
def update_data():
    data = {
        'id' : 4,
        'name' : 'manish',
        'city' : 'ranchi' 
    }
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)


# update_data()
def delete_data():
    data = {'id': 3}
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    r = requests.delete(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)

delete_data()

