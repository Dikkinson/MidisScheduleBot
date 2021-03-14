from aiogram import types

from utils.db_api import Users
from utils.misc.weeks import get_week

from loader import dp

import emoji

from utils.misc import rate_limit

@dp.message_handler(text="/sub", state='*')
@rate_limit(1)
async def user_switch_sub(message: types.Message):
    if await Users.is_sub(message.from_user):
        await message.answer(f"Ты отписался от расслыки 💔\n"
                             f"Чтобы подписаться обратно /sub 📞")
    else:
        await message.answer(f"Ты подписался на расслыку ❤️\n"
                             f"📵 Чтобы отписаться /sub")
    await Users.switch_sub(message.from_user)


@dp.message_handler(text="📆 Какая сейчас неделя?", state='*')
@rate_limit(1)
async def bot_echo(message: types.Message):
    await message.answer(f"Сейчас {'Вторая' if get_week() else 'Первая'} неделя")


@dp.message_handler(text="Пошёл нахуй", state='*')
async def bot_echo(message: types.Message):
    await message.answer(emoji.emojize(f"Сам пошёл нахуй :clown_face:", use_aliases=True))


@dp.message_handler(state='*')
@rate_limit(1)
async def bot_echo(message: types.Message):
    await message.answer(emoji.emojize(f"Я не понял что ты написал :pensive:\n"
                                       f"Если что, напиши /help", use_aliases=True))
