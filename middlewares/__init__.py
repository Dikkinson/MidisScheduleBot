from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .logger import LoggingMiddleware
from .add_user import UsersMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(UsersMiddleware())
    dp.middleware.setup(LoggingMiddleware())
