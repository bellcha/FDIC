import requests as rq
import json
import pandas as pd
from dataclasses import dataclass, asdict

@dataclass
class MMBKData:
    REPDTE: str
    ASSET: int
    EEFFQR: float

url = 'https://banks.data.fdic.gov/api/financials?filters=CERT%3A12203&fields=REPDTE%2CASSET%2CEEFFQR&sort_by=REPDTE&sort_order=DESC&limit=10000&offset=0&agg_limit=1&format=json&download=false&filename=data_file'

data = rq.get(url).text

json_data = json.loads(data)

mmbk_df = pd.DataFrame(columns=['REPDTE','ASSET','EEFFQR'])


for d in json_data['data']:
    results = MMBKData(REPDTE=d['data']['REPDTE'], ASSET=d['data']['ASSET'], EEFFQR=d['data']['EEFFQR'])
    row = pd.DataFrame(asdict(results), index=[0])
    mmbk_df = pd.concat([mmbk_df,row], axis=0 ,ignore_index=True)

print(mmbk_df.head(5))

mmbk_df.to_excel('eff_hist.xlsx', index= False)
