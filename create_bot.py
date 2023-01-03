from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

import config
from services.parser_vk_service import VKParser
from services.database_service import Database

# Задаём уровень логов
logging.basicConfig(level=logging.INFO)


# Создаём бота и диспатчер
bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


# Создаём инстансы сервисов
vk_parser = VKParser(token=config.VK_TOKEN)
mongo = Database(config.MONGODB_URI)

