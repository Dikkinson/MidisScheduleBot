from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from data import config
from utils.misc.parser import Parser
import logging
# Configure logging
logging.basicConfig(level=logging.DEBUG)

parser = Parser('rasp.xlsx')
rasp = parser.get_rasp()
old_file_id = ['0']
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# storage = RedisStorage(host='rediska')
storage = RedisStorage()
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()
