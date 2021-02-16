import requests
import json
URL = "http://127.0.0.1:8000/stu/"
# #this is my application to get data from my API
# r=requests.get(url=URL)
# data = r.json()
# print(data)

def get_data(id=None):
    data = {}
    if id is not None:
        data= {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data = json_data)
    data = r.json()
    print(data)
# get_data()

def post_data():
    data ={
        'name':'Ram',
        'roll':105,
        'city':'Mumbai'
    }
    json_data =json.dumps(data)
    r =requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)
post_data()

def put_data():
    data ={
        'id':1,
        'name':'vineet',
        'roll':100,
        'city':'delhi'
    }
    json_data = json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    json_data =r.json()
    print(json_data)
# put_data()

def delete_data():
    data={'id':1}
    json_data = json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data = r.json()
    print(data)

# delete_data()