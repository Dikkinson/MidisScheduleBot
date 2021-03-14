from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❗️Сегодня"),
            KeyboardButton(text="❕Завтра")
        ],
        [
            KeyboardButton(text="▶️ Текущая неделя"),
            KeyboardButton(text="⏩ Следующая неделя")
        ],
        [
            KeyboardButton(text="👨‍👧‍👦Расписание других групп"),
        ]
    ],
    resize_keyboard=True
)
