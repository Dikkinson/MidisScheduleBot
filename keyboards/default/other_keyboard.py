from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

other_markup = ReplyKeyboardMarkup(
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
            KeyboardButton(text="👨‍🎓 Вернуться к своему расписанию")
        ]
    ],
    resize_keyboard=True
)
