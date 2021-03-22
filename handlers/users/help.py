from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    text = ("Если что- то сломалось, то просто напиши команду: /start\n"
            "Бот обнулится - и всё будет как надо 👍\n"
            "На крайняк напиши разработчикам, контакты в профиле 😘")
    await message.answer(text)
