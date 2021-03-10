from aiogram.dispatcher import FSMContext
from keyboards.default import other_markup
from loader import dp
from aiogram.types import Message, CallbackQuery
from loader import rasp
from datetime import datetime, timedelta
from utils.misc.schedule_creator import create_rasp_text
from states import User_form
from utils.misc import rate_limit
from utils.misc.weeks import get_week
from handlers.users.user_schedule import rasp_today
from keyboards.inline.callback_datas import study_year_callback
from keyboards.default.groups_keybard import select_groups_to_show
import emoji


@dp.callback_query_handler(study_year_callback.filter(button_func="other_study_year"), state='*')
async def other_selected_study_year(call: CallbackQuery, callback_data: dict):
    # Ставим стейт выбора группы юзера
    await User_form.other_group.set()
    await call.answer(cache_time=0)
    await call.message.answer(emoji.emojize(f"Выбран {callback_data.get('number')} курс\n"
                                            f"Теперь выбери группу :book:", use_aliases=True),
                              reply_markup=select_groups_to_show(callback_data.get("number")))


@dp.message_handler(text=rasp[0].keys(), state=User_form.other_group)
async def other_select_group(message: Message, state: FSMContext):
    await state.update_data(other_group=message.text)
    await other_rasp_today(message, state)


@dp.message_handler(text="❗️Сегодня", state=User_form.other_group)
@rate_limit(2)
async def other_rasp_today(message: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            await message.answer(f"Расписание на сегодня:\n\n"
                                 f"{rasp[get_week()][data['other_group']][datetime.today().weekday()]}", reply_markup=other_markup)
        except KeyError:
            await message.answer("Сегодня пар нет 🥳", reply_markup=other_markup)


@dp.message_handler(text="❕Завтра", state=User_form.other_group)
@rate_limit(2)
async def other_rasp_tomorrow(message: Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            tomorrow = datetime.today() + timedelta(days=1)
            await message.answer(f"Расписание на завтра:\n\n"
                                 f"{rasp[get_week()][data['other_group']][tomorrow.weekday()]}")
        except KeyError:
            await message.answer("Завтра пар нет 🥳")


@dp.message_handler(text="1️⃣ неделя", state=User_form.other_group)
@rate_limit(2)
async def other_rasp_first_week(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(text=create_rasp_text(0, data['other_group'], rasp))


@dp.message_handler(text="2️⃣ неделя", state=User_form.other_group)
@rate_limit(2)
async def other_rasp_second_week(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(text=create_rasp_text(1, data['other_group'], rasp))


@dp.message_handler(text="👨‍🎓 Вернуться к своему расписанию", state=User_form.other_group)
@rate_limit(2)
async def back_user_group(message: Message, state: FSMContext):
    await User_form.user_group.set()
    await rasp_today(message, state)
