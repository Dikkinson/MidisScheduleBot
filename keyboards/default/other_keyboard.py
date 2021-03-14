from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

other_markup = ReplyKeyboardMarkup(
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
            KeyboardButton(text="👨‍🎓 Вернуться к своему расписанию"),
        ]
    ],
    resize_keyboard=True
)
