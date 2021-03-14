from aiogram.dispatcher.filters.state import StatesGroup, State


class User_form(StatesGroup):
    user_study_year = State()
    user_group = State()
    default_state = State()
    other_study_year = State()
    other_group = State()
