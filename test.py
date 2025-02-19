from parsers.utils import parse_rus_date

import pandas as pd

test_data = pd.DataFrame([
    '14 мая, 09:58', '14:19', '12 мая, 13:09', '13 мая, 12:05', '10 мая, 11:48',
    '11 мая, 11:38', '13:54', 'Вчера, 10:05', '14 мая, 10:08',
    'Вчера, 08:00', '14 мая, 09:05', 'Вчера, 06:51', 'Вчера, 05:28',
    '14:43', 'Вчера, 16:53', '16 марта 2020, 23:03', '12 февраля 2021, 15:11',
    '25 декабря 2023, 15:23', '18 июня 2023, 01:21', '22 апреля 2021, 11:00',
    '14 мая, 14:11', '11 августа 2021, 21:09', '26 апреля 2020, 17:38',
     '9 марта 2020, 23:15', '9 июня 2023, 15:11', '7 июля 2022, 21:42',
    '28 апреля 2023, 15:33', '24 марта, 22:17', '28 октября 2022, 17:12',
    '24 июля 2022, 17:28', '19 января 2021, 00:19', '9 сентября 2020, 21:36'
    ], columns=['unparsed'])

test_data['parsed'] = test_data.unparsed.apply(parse_rus_date)

print(test_data)