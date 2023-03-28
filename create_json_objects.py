import os
import requests
import json

entities = ['services', 'routes', 'consumers', 'plugins', 'certificates', 'ca_certificates', 'snis', 'upstreams', 'targets', 'vaults', 'keys', 'licenses', 'developers', 'consumer_groups']

if not os.path.exists('entities'):
    os.makedirs('entities')

for entity in entities:
    response = requests.get(f'http://localhost:8001/schemas/{entity}')

    if response.status_code != 200:
        print(f"Error {entity}. Response code: {response.status_code}")
    else:
        response_json = json.loads(response.text)
        with open(f'entities/{entity}.json', 'w') as f:
            json.dump(response_json, f, indent=2)