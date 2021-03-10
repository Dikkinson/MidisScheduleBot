from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сегодня"),
            KeyboardButton(text="Завтра")
        ],
        [
            KeyboardButton(text="Первая неделя"),
            KeyboardButton(text="Вторая неделя")
        ],
        [
            KeyboardButton(text="Расписание других групп")
        ]
    ],
    resize_keyboard=True
)
