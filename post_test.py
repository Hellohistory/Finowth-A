import requests
import json

url = 'http://localhost:36925/stock_szse_summary'
data = {
    'date': "20240717"
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)
