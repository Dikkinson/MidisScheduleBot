from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

import emoji

from utils.misc import rate_limit


@dp.message_handler(text="Пошёл нахуй", state='*')
async def bot_echo(message: types.Message):
    await message.answer(emoji.emojize(f"Сам пошёл нахуй :clown_face:", use_aliases=True))


@dp.message_handler(state='*')
@rate_limit(1)
async def bot_echo(message: types.Message):
    await message.answer(emoji.emojize(f"Я не понял что ты написал :pensive:\n"
                                       f"Если что, напиши /help", use_aliases=True))