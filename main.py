from parsers.prime import PrimeParser
import pandas as pd

parser = PrimeParser()

print(parser.get_news_by_period('прибыль', date_from=pd.to_datetime('2024-05-15 21:36:00'), sortby='date'))