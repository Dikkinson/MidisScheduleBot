from aiogram import executor
import middlewares, filters, handlers
from loader import dp, scheduler, rasp, old_file_id
from utils.notify_admins import notify_admins_def
from middlewares.throttling import ThrottlingMiddleware
from datetime import datetime, timedelta
from utils.notify_subscribers import broadcaster


async def on_startup(dispatcher):
    scheduler.add_job(
        broadcaster, args=(dp, rasp), trigger='interval', hours=24,
        next_run_time=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(hours=8)
    )
    scheduler.start()
    # Уведомляет про запуск
    await notify_admins_def(dispatcher, "Я запустился")


async def on_shutdown(dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()
    await notify_admins_def(dispatcher, "Я выключился")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
