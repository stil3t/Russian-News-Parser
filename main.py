from parsers.prime import PrimeParser
from parsers.rbc import RBCParser

from parsers.utils import news_df_to_txt

import datetime as dt

import pandas as pd

prime_parser = PrimeParser()
rbc_parser = RBCParser()

prime_news = prime_parser.get_last_news('прибыль')
# prime_news = prime_parser.get_news_by_period(
#     'прибыль', 
#     date_from=pd.to_datetime('2024-05-15'), 
#     date_to=pd.to_datetime('2024-05-18'), 
#     sortby='date'
# )
print(news_df_to_txt(prime_news))


rbc_news = rbc_parser.get_last_news('прибыль')
# rbc_news = rbc_parser.get_news_by_period(
#     'прибыль', 
#     date_from=pd.to_datetime('2024-05-15'), 
#     date_to='now' #pd.to_datetime('2024-05-18')
# )
print(news_df_to_txt(rbc_news))

# import requests

# url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

# payload={
#   'scope': 'GIGACHAT_API_PERS'
# }
# headers = {
#   'Content-Type': 'application/x-www-form-urlencoded',
#   'Accept': 'application/json',
#   'RqUID': '04c4fb08-dfd1-46bf-a8ad-3c9c2668c355',
#   'Authorization': 'Basic <Authorization key>'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

# import requests

# url = "https://gigachat.devices.sberbank.ru/api/v1/models"

# payload={}
# headers = {
#   'Accept': 'application/json',
#   'Authorization': 'Bearer <Access token>'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)