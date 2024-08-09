import requests
import json

url = 'http://localhost:36925/config'
data = {
    "config_type": "db",
    "db_config": {
        "db_type": "mysql",
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "hellohistory"
    }
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)
