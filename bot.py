import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from parsers.prime import PrimeParser
from parsers.rbc import RBCParser

from parsers.utils import news_df_to_txt

from gigachat import GigaChat

load_dotenv()
TOKEN = getenv("BOTKEY")
GIGIAKEY = getenv('GIGIAKEY')


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Ку, {html.bold(message.from_user.full_name)}!\n"
                         "Я прототип сжиматора новостей 3000 про плюс супер 5 Джи\n"
                         "По какой конторе проконсультировать?")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        parser = PrimeParser()
        news = parser.get_last_news(message.text, period='month')
        
        if len(news) < 1:
            await message.answer('За последний месяц новостей не найдено')

        else:
            query =\
            f'Оцени новостной фон для компании {message.text} и скажи,'\
            ' стоит ли покупать акции этой компании.'\
            'В твоем ответе не должно быть больше 150 слов. При ответе опирайся на следующие новости:'\
            + news_df_to_txt(news)

            with GigaChat(credentials=GIGIAKEY, verify_ssl_certs=False) as giga:
                response = giga.chat(query)
                response = response.choices[0].message.content
            
            await message.answer(response + '\nНе является ИИР!!')


    except TypeError:
        await message.answer("Что-то пошло не так!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())