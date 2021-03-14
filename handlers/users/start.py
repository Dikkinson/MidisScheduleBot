from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.groups_keybard import select_groups_to_show
from keyboards.inline import study_years_markup
from keyboards.inline.callback_datas import study_year_callback
from loader import rasp
from handlers.users.user_schedule import rasp_today
from utils.db_api import Users
from utils.misc import rate_limit

from states import User_form
import emoji


@dp.message_handler(CommandStart(), state='*')
@rate_limit(0.5)
async def bot_start(message: Message):
    # Ставим стейт выбора курса юзера
    await User_form.user_study_year.set()
    await message.answer(emoji.emojize(f"Привет, {message.from_user.first_name} :hand:\n"
                                       f"Я бот МИДиС помогу узнать твоё расписание :calendar:\n"
                                       f"Для начала, на каком курсе ты учишься? :mortar_board:", use_aliases=True),
                         reply_markup=study_years_markup)


@dp.callback_query_handler(study_year_callback.filter(button_func="study_year"), state='*')
@rate_limit(0.5)
async def selected_study_year(call: CallbackQuery, callback_data: dict):
    # Ставим стейт выбора группы юзера
    await User_form.user_group.set()
    await call.answer(cache_time=0)
    await call.message.answer(emoji.emojize(f"Выбран {callback_data.get('number')} курс\n"
                                            f"Теперь выбери свою группу :book:", use_aliases=True),
                              reply_markup=select_groups_to_show(callback_data.get("number")))


@dp.message_handler(text=rasp[0].keys(), state=User_form.user_group)
@rate_limit(0.5)
async def select_group(message: Message, state: FSMContext):
    await state.update_data(user_group=message.text)
    await Users.set_group(message.text, message.from_user)
    await Users.set_sub(message.from_user)
    await rasp_today(message, state)
    await User_form.default_state.set()
