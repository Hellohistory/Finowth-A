import requests
import json

url = 'http://127.0.0.1:36925/stock_zh_b_daily'
data = {
    "symbol": "sh900901",
    "start_date": "20101103",
    "end_date": "20201116",
    "adjust": "qfq"
}
response = requests.post(url, json=data)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)
