import json

import requests

session = requests.Session()
session.auth = ('x', 'x')
response = session.get('')


# print(json.dumps(response.json(), sort_keys=True,
#                   indent=4, separators=(',', ': ')))

json_response = json.dumps(response.json())
json_parse = json.loads(json_response)

print(type(json_parse['result']['Data']))
#print(json_parse.get('result'))
