from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import rasp

groups_markup = ReplyKeyboardMarkup(one_time_keyboard=True)


def select_groups_to_show(study_year):
    groups_markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    for group in rasp[0].keys():
        if group[group.index("-") + 1] == str(study_year):
            button = KeyboardButton(text=group)
            groups_markup.insert(button)
    return groups_markup
