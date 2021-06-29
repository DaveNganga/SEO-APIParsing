# sample requests file and json parsor
import requests
import json

file = requests.get("http://api.open-notify.org/astros.json")

json_file = file.json()

print("Status Code: ", file.status_code)

counter = 0
for Key in json_file['people']:
    if counter == 5:
        break
    print(Key['name'])
    counter += 1
