from aiogram.dispatcher import FSMContext
from keyboards.default import user_markup
from loader import dp
from aiogram.types import Message, CallbackQuery
from loader import rasp
from datetime import datetime, timedelta
from utils.misc.schedule_creator import create_rasp_text
from states import User_form
from utils.misc import rate_limit
from utils.misc.weeks import get_week
from keyboards.inline import study_years_markup, other_study_years_markup
from keyboards.inline.callback_datas import study_year_callback
from keyboards.default.groups_keybard import select_groups_to_show
import emoji


@dp.message_handler(text="❗️Сегодня", state=User_form.default_state)
@rate_limit(0.5)
async def rasp_today(message: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            await message.answer(f"Расписание на сегодня:\n\n"
                                 f"{rasp[get_week(datetime.today())][data['user_group']][datetime.today().weekday()]}",
                                 reply_markup=user_markup)
        except KeyError:
            await message.answer("Сегодня пар нет 🥳", reply_markup=user_markup)


@dp.message_handler(text="❕Завтра", state=User_form.default_state)
@rate_limit(0.5)
async def rasp_tomorrow(message: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            tomorrow = datetime.today() + timedelta(days=1)
            await message.answer(f"Расписание на завтра:\n\n"
                                 f"{rasp[get_week(tomorrow)][data['user_group']][tomorrow.weekday()]}", reply_markup=user_markup)
        except KeyError:
            await message.answer("Завтра пар нет 🥳", reply_markup=user_markup)


@dp.message_handler(text="▶️ Текущая неделя", state=User_form.default_state)
# @rate_limit(0.5)
async def rasp_first_week(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(text=create_rasp_text(get_week(datetime.today()), data['user_group'], rasp))


@dp.message_handler(text="⏩ Следующая неделя", state=User_form.default_state)
# @rate_limit(0.5)
async def rasp_second_week(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(text=create_rasp_text(int(not get_week(datetime.today())), data['user_group'], rasp))


@dp.message_handler(text="👨‍👧‍👦Расписание других групп", state=User_form.default_state)
@rate_limit(0.5)
async def rasp_other_group(message: Message):
    await User_form.other_study_year.set()
    await message.answer(emoji.emojize(f"Выбери курс группы, у которой ты хочешь посмотреть расписание :mortar_board:", use_aliases=True),
                         reply_markup=other_study_years_markup)
