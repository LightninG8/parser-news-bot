from aiogram import executor
import asyncio

from create_bot import dp, vk_parser, bot
from handlers.scheduled import scheduled

async def on_startup(_):
	loop = asyncio.get_event_loop()
	loop.create_task(scheduled.scheduled(10))

	print('Bot has been started')



if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
