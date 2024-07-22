import requests
import json

url = 'http://127.0.0.1:36925/stock_hsgt_hold_stock_em'
data = {
    "market": "沪股通",
    "indicator": "3日排行"

}
response = requests.post(url, json=data)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)
