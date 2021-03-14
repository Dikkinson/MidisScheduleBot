import asyncio

from aiogram import Dispatcher
from aiogram.utils import exceptions
import logging

from utils.db_api import Users
from utils.misc.weeks import get_week
from datetime import datetime

log = logging.getLogger('broadcast')


async def broadcaster(dp, rasp) -> int:
    """
    Simple broadcaster

    :return: Count of messages
    """
    if datetime.today().weekday() == 6:
        return 0

    count = 0
    try:
        for user in await Users.get_sub():
            group = await Users.get_group(user['user_id'])
            try:
                text = f"Расписание на сегодня:\n\n" \
                       f"{rasp[get_week()][group][datetime.today().weekday()]}\n" \
                       f"📵 Чтобы отписаться от ежедвневной рассылки /sub"
            except KeyError:
                text = "Сегодня пар нет 🥳\n" \
                       "📵 Чтобы отписаться от ежедвневной рассылки /sub"
            if await send_message(dp, user['user_id'], text):
                count += 1
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        log.info(f"{count} messages successful sent.")

    return count


async def send_message(dp: Dispatcher, user_id: int, text: str) -> bool:
    try:
        await dp.bot.send_message(user_id, text)
    except exceptions.BotBlocked:
        log.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        log.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message(dp, user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        log.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        log.exception(f"Target [ID:{user_id}]: failed")
    else:
        log.info(f"Target [ID:{user_id}]: success")
        return True
    return False
