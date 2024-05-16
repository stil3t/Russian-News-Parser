import datetime as dt

RUS_MONTHS = [
    'января', 'февраля', 
    'марта', 'апреля', 'мая', 
    'июня', 'июля', 'августа', 
    'сентября', 'октября', 'ноября',
    'декабря'
]
RUS_MONTHS = dict(zip(RUS_MONTHS, range(1, 13)))

DAY = dt.timedelta(days=1)


def parse_rus_date(s):
    s = str(s)\
        .replace(',', ' ')\
        .replace(':', ' ')\
        .lower()\
        .split()

    if 'вчера' in s:
        yesterday = dt.datetime.today() - DAY
        return dt.datetime(yesterday.year, yesterday.month, yesterday.day, int(s[-2]), int(s[-1]))

    elif len(s) == 2:
        today = dt.datetime.today()
        return dt.datetime(today.year, today.month, today.day, int(s[-2]), int(s[-1]))

    elif len(s) == 5:
        if month_num := RUS_MONTHS.get(s[1]):
            s[1] = month_num

        s = list(map(int, s))
        return dt.datetime(s[2], s[1], s[0], s[-2], s[-1])
    
    elif len(s) == 4:
        if month_num := RUS_MONTHS.get(s[1]): 
            s[1] = month_num

        s = list(map(int, s))
        return dt.datetime(2024, s[1], s[0], s[-2], s[-1])
    
    else:
        raise NotImplementedError
    