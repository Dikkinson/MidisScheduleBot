import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def notify_admins_def(dp: Dispatcher, text : str):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, text=text)

        except Exception as err:
            logging.exception(err)

# async def on_startup_notify(dp: Dispatcher):
#     for admin in ADMINS:
#         try:
#             await dp.bot.send_message(admin, "Я запустился")
#
#         except Exception as err:
#             logging.exception(err)
#
#
# async def on_shutdown_notify(dp: Dispatcher):
#     for admin in ADMINS:
#         try:
#             await dp.bot.send_message(admin, "Я выключился")
#
#         except Exception as err:
#             logging.exception(err)
