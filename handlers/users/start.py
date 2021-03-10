from aiogram.dispatcher import FSMContext
from keyboards.default import user_markup
from loader import dp
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.groups_keybard import select_groups_to_show
from keyboards.inline import study_years_markup
from keyboards.inline.callback_datas import study_year_callback
from loader import rasp
from datetime import datetime, timedelta

from states import User_form
import emoji


def create_rasp_text(week: int, group_name: str):
    text = f"Расписание на {'вторую' if week else 'первую'} неделю {group_name}:\n\n"
    for day in rasp[week][group_name]:
        text += f"<i>{days[day]}</i>\n"
        try:
            text += f"{rasp[week][group_name][day]}\n"
        except KeyError:
            pass
    return text


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.chat.id
    await message.answer(emoji.emojize(f"Привет, {message.from_user.first_name} :hand:\n"
                                       f"Я бот МИДиС помогу узнать твоё расписание :calendar:\n"
                                       f"Для начала, на каком курсе ты учишься? :mortar_board:", use_aliases=True),
                         reply_markup=study_years_markup)


@dp.callback_query_handler(study_year_callback.filter(button_func="study_year"), state='*')
async def selected_study_year(call: CallbackQuery, callback_data: dict):
    # Ставим стейт выбора группы юзера
    await User_form.user_group.set()
    await call.answer(cache_time=0)
    await call.message.answer(emoji.emojize(f"Выбран {callback_data.get('number')} курс\n"
                                            f"Теперь выбери свою группу :book:", use_aliases=True),
                              reply_markup=select_groups_to_show(callback_data.get("number")))


@dp.message_handler(text=rasp[0].keys(), state='*')
async def select_group(message: Message, state: FSMContext):
    await state.update_data(user_group=message.text)
    await rasp_today(message, state)
