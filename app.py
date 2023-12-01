import requests
import json
import random
response_API = requests.get('https://github.com/rakhadjo/tyrannosaurus.rest.git')

print(response_API.text) 

