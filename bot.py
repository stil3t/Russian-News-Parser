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

from parsers.utils import build_query

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
        query = build_query(message.text, parser)

        with GigaChat(credentials=GIGIAKEY, verify_ssl_certs=False) as giga:
            response = giga.chat(query)
            response = response.choices[0].message.content
            
        await message.answer(response)


    except TypeError:
        await message.answer("Что-то пошло не так!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())