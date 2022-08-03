import requests as rq
import json
url = 'https://banks.data.fdic.gov/api/financials?filters=CERT%3A12203&fields=CERT%2CREPDTE%2CASSET%2CEEFFQR&sort_by=REPDTE&sort_order=DESC&limit=10000&offset=0&agg_limit=1&format=json&download=false&filename=data_file'

data = rq.get(url).text


json_data = json.loads(data)


for d in json_data['data']:
    print(d['data'])
