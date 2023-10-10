from config import TOKEN, database_cred
import asyncio
import logging
import sys
import os


from aiogram import Bot, Dispatcher, F
from aiogram import types
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from translator import translate

from db import Database

bot = Bot(TOKEN)
dp = Dispatcher()

if os.name == 'posix':
    database_cred['host'] = '172.17.0.1'
db = Database()



@dp.message(F.text == '/start')
async def start(message: Message):
    await message.answer('Привет! Я переводчик с русского на английский язык. Напиши слово или предложение, которое хочешь перевести на английский язык')


@dp.message(F.text == '/admin')
async def admin(message: Message):
    result = db.get_users()
    builder = InlineKeyboardBuilder()
    for elem in result:
        builder.button(text=elem[0], callback_data=elem[0])
    builder.adjust(1, 1)
    await message.reply('Выберите чью историю переводов хотите посмотреть', reply_markup=builder.as_markup())


@dp.callback_query()
async def send_information(callback: types.CallbackQuery):
    result = db.get_info_about_user(callback.data)
    for elem in result:
        await callback.message.answer(f'{callback.data} просил перевести {elem[1]} и получил в ответ {elem[2]}')


@dp.message()
async def work(message: Message):
    res = translate(message.text)
    await message.answer(res)
    db.add_info(message.from_user.full_name,
                             message.text,
                             res)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
