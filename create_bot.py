from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

import config
from services.parser_service import Parser
from services.database_service import Database

# Задаём уровень логов
logging.basicConfig(level=logging.INFO)


# Создаём бота и диспатчер
bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
mongo = Database(config.MONGODB_URI)


# Создаём инстансы сервисов
parser = Parser(lastkey_file='lastkey.txt', token=config.VK_TOKEN)
