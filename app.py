import requests
import json
response_API = requests.get('https://github.com/shultztom/dinosaur-fact-api/.git')
#print(response_API.status_code) 
data = json.loads(response_API.text)

value = data['key']

print(value)