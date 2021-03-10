from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage

from data import config
from utils.misc.parser import Parser

parser = Parser('Расписание на 05.03.21.xlsx')
rasp = parser.get_rasp()
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = RedisStorage()
dp = Dispatcher(bot, storage=storage)
