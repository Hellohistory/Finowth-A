import requests
import json

url = 'http://127.0.0.1:36925/stock_hk_spot_em'

response = requests.get(url)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)
