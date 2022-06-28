import requests
import json

ENDPOINT: str = 'https://api.spacexdata.com/v5/launches/latest'

my_request = requests.get(ENDPOINT)

status_code: int = my_request.status_code
message: str = json.loads(my_request.content)

if (status_code == 200):
    print("THE API WORKS")
else:
    print(':*(')

print(message)
print(message['links']['reddit']['id'])

id_needed: int = message['links']['reddit']['id']

my_request = requests.get(ENDPOINT+str(id_needed))