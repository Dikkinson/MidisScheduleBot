from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify, on_shutdown_notify

from middlewares.throttling import ThrottlingMiddleware


async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()
    await on_shutdown_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
