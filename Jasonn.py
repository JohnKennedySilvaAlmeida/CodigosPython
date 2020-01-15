import json
#import simplejson as json

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

parsed_json = json.loads(json_string)

print(parsed_json['first_name'])
"Guido"

print()

d = {
    'first_name': 'Guido',
    'second_name': 'Rossum',
    'titles': ['BDFL', 'Developer'],
}

print(json.dumps(d))
'{"first_name": "Guido", "last_name": "Rossum", "titles": ["BDFL", "Developer"]}'