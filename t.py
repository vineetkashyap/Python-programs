import requests
URL = "http://127.0.0.1:8000/stu/"
#this is my application to get data from my API
r=requests.get(url=URL)
data = r.json()
print(data)
