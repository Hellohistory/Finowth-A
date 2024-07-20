import requests
import json

url = 'http://127.0.0.1:36925/stock_szse_area_summary'
payload = {
    "ym_date": "202406"
}
response = requests.post(url, json=payload)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)