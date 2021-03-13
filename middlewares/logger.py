from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.db_api import Logs


class LoggingMiddleware(BaseMiddleware):
    def __init__(self):
        super(LoggingMiddleware, self).__init__()

    @staticmethod
    async def on_process_message(message: types.Message, data: dict):
        await Logs.log_message(message)
