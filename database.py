from uuid import uuid4

async def init_db():
    """Проверить подключение, создать таблички, если их нет."""
    pass

async def insert_query(text, user=None):
    """Нужно хранить uuid, время запроса (точность до секунды хватит), хэш текста, текст, id пользователя"""
    uid = uuid4()
    hashed_text = hash(text.lower())

    return uid

async def insert_response(text, query_uid, model='GigaChat', was_useful=None):
    """Нужно хранить uuid, uid запроса, время ответа (точности до секунды хватит), модель, флаг полезности ответа, текст ответа"""
    uid = uuid4()
    pass

async def reuse_response(text):
    hashed_text = hash(text.lower())
    # ищем хэш запроса в табличке предыдущих. 
    # Берем только свежие - последние полчаса (в будущем можно уменьшить). Ну и предпочтение флагам полезности
    # Что-то вроде ROW_NUMBER() OVER (PARTITION BY ... ORDER BY response_dt DESC, useful DESC) as rown и потом where rown = 1
    # не нашли - возвращаем None
    return None