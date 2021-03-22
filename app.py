from aiogram import executor
import middlewares, filters, handlers
from loader import dp, scheduler, rasp, old_file_id
from utils.notify_admins import notify_admins_def
from middlewares.throttling import ThrottlingMiddleware
from datetime import datetime, timedelta
from utils.notify_subscribers import broadcaster
from utils.portal_parser import get_rasp


async def on_startup(dispatcher):
    scheduler.add_job(
        broadcaster, args=(dp, rasp), trigger='interval', hours=24,
        next_run_time=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(hours=3)
    )
    scheduler.add_job(get_rasp, args=(rasp, old_file_id, dp), trigger='interval', hours=1, next_run_time=datetime.now())
    scheduler.start()
    # Уведомляет про запуск
    await notify_admins_def(dispatcher, "Я запустился")


async def on_shutdown(dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()
    await notify_admins_def(dispatcher, "Я выключился")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
