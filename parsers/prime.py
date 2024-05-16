from .utils import parse_rus_date
import pandas as pd
import requests

import bs4
from urllib.parse import quote_plus

from time import sleep
import datetime as dt

"""
Парсер создан только для личных некоммерческих (учебных и исследовательских) целей.

В случае нарушения прав свяжитесь со мной любым доступным способом:

TG: https://t.me/rooted_ios
VK: https://vk.com/xugoo
email: galliy7rezerford@gmail.com

https://1prime.ru/docs/terms_terms_of_use.html
© 1996-2024 АО "АЭИ "ПРАЙМ"". Все права защищены.
"""

class PrimeParser:

    def __init__(self):
        pass

    def get_news_by_period(self, query, date_from, date_to='now', max_pages=1, sortby='relevance'):

        query = quote_plus(query)

        if date_to in ['now', 'today']:
            date_to = dt.datetime.now()

        if sortby in ['relevance', 'rel', 'r']:
            sortby = 'relevance'
        elif sortby in ['datetime', 'time', 'date', 'd']:
            sortby = 'date'

        news = []

        for i in range(max_pages):
            offset = f'&offset={20 * i}' if i > 0 else ''
            req = requests.get('https://1prime.ru/services/search/getmore/'
                                '?tags_limit=10'
                                f'&date_from={str(date_from.date())}'
                                f'&date_to={str(date_to.date())}'
                                f'&query={query}'
                                f'{offset}'
                                '&sort={sortby}')
            sleep(0.05)
                
            content = bs4.BeautifulSoup(req.content, 'html.parser')
            content = self.process_news_page(content)

            if not content:
                break
                
            news.extend(content)
                            
        return pd.DataFrame(news, columns=['title', 'datetime'])
    
    @staticmethod
    def process_news_page(page):

        found = page.find(attrs={'class': 'list-items-loaded'}).get('data-count')        
        if not found or found == '0':
            return []
        
        news = page.find_all(attrs={'class': 'list-item'})
        titles = []
        for item in news:
            res = item.find(attrs={'class': 'list-item__title'})
            
            title = ''
            for elem in res:
                if type(elem) != bs4.element.NavigableString:
                    title += elem.contents[0]
                    continue
                else:
                    title += elem
            date = item.find(attrs={'class': 'list-item__date'}).contents[0]

            titles.append((title, parse_rus_date(date)))

        return titles