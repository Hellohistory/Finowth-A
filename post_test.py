import requests
import json

url = 'http://127.0.0.1:36925/stock_report_fund_hold'
data = {
    "symbol": "基金持仓",
    "date": "20200630"
}
response = requests.post(url, json=data)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)
