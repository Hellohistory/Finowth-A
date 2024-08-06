import requests
import json

url = 'http://localhost:36925/stock_board_concept_hist_em'
data = {
    'symbol': "租售同权",
    'period': "daily",
    'start_date': "20240701",
    'end_date': "20240708",
    'adjust': ""
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(response.status_code)
