from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❗️Сегодня"),
            KeyboardButton(text="❕Завтра")
        ],
        [
            KeyboardButton(text="1️⃣ неделя"),
            KeyboardButton(text="2️⃣ неделя")
        ],
        [
            KeyboardButton(text="👨‍👧‍👦Расписание других групп")
        ]
    ],
    resize_keyboard=True
)
