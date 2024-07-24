import requests
import json

url = 'http://localhost:36925/stock_zh_a_disclosure_report_cninfo'
data = {
    'symbol': "000001",
    'market': "港股",
    'keyword': "",
    'category': "半年报",
    'start_date': "20230618",
    'end_date': "20231219"
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)
