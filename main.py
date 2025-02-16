from parsers.prime import PrimeParser
from parsers.rbc import RBCParser

from parsers.utils import news_df_to_txt

import datetime as dt

import pandas as pd

prime_parser = PrimeParser()
rbc_parser = RBCParser()

prime_news = prime_parser.get_last_news('МТС Банк', period='month')
# prime_news = prime_parser.get_news_by_period(
#     'прибыль', 
#     date_from=pd.to_datetime('2024-05-15'), 
#     date_to=pd.to_datetime('2024-05-18'), 
#     sortby='date'
# )
print(news_df_to_txt(prime_news))

# print('='*100)

# rbc_news = rbc_parser.get_last_news('прибыль')
# # rbc_news = rbc_parser.get_news_by_period(
# #     'прибыль', 
# #     date_from=pd.to_datetime('2024-05-15'), 
# #     date_to='now' #pd.to_datetime('2024-05-18')
# # )
# print(news_df_to_txt(rbc_news))

