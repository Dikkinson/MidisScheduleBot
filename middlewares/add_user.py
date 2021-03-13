from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.db_api import Users


class UsersMiddleware(BaseMiddleware):
    def __init__(self):
        super(UsersMiddleware, self).__init__()

    @staticmethod
    async def on_process_message(message: types.Message, data: dict):
        await Users.set_user(message.from_user)
