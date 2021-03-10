from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji

from keyboards.inline.callback_datas import study_year_callback

study_years_markup = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text=emoji.emojize(":one:", use_aliases=True), callback_data="study_year:study_year:1"),
            InlineKeyboardButton(text=emoji.emojize(":two:", use_aliases=True), callback_data="study_year:study_year:2"),
            InlineKeyboardButton(text=emoji.emojize(":three:", use_aliases=True), callback_data="study_year:study_year:3"),
            InlineKeyboardButton(text=emoji.emojize(":four:", use_aliases=True), callback_data="study_year:study_year:4")
        ]
    ],
    resize_keyboard=True
)
