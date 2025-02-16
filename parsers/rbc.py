from .utils import parse_rus_date
import pandas as pd
import requests
import json

from urllib.parse import quote_plus

from time import sleep
import datetime as dt

from dotenv import load_dotenv
from os import getenv

"""
код в чистом виде работать не будет: умышленно вырезана важная часть
"""

class RBCParser:

    def __init__(self):
        load_dotenv()
        pass
    
    def get_last_news(self, query, period='week'):
        if period in ['week', 'w']:
            date_from = dt.datetime.now() - dt.timedelta(days=7)
        elif period in ['month', 'm']:
            date_from = dt.datetime.now() - dt.timedelta(days=30)
        else:
            date_from = dt.datetime.now() - dt.timedelta(days=1)

        return self.get_news_by_period(query, date_from=date_from)


    def get_news_by_period(self, query, date_from, date_to='now', max_pages=1):

        query = quote_plus(query)

        if date_to in ['now', 'today']:
            date_to = pd.to_datetime(dt.datetime.now())
        
        news = []
        
        for page in range(max_pages):
            url =\
                getenv('RBC_VYREZNYA') \
                + f'?query={query}'\
                + f'&dateFrom={str(date_from.strftime('%d.%m.%Y'))}'\
                + f'&dateTo={str(date_to.strftime('%d.%m.%Y'))}'\
                + f'&page={page}'
            req = requests.get(url)
            
            content = json.loads(req.content)
            sleep(0.01)
                            
            news.extend(content['items'])
                
            if not content['moreExists']:
                    break
            
        news = pd.DataFrame(news)[['title', 'body', 'publish_date']]
        news.publish_date = pd.to_datetime(news.publish_date, format='mixed', utc=True)  #.dt.tz_localize(None)

        return news
    