
import asyncio
import aioschedule

from create_bot import mongo
from .parser.vk.vk import parse_vk

async def check_new_posts():
    users = mongo.get_users()

    for user in users:
      await parse_vk(user)


async def scheduled(delay):
  aioschedule.every(delay).seconds.do(check_new_posts)

  while True:
    await aioschedule.run_pending()
    await asyncio.sleep(1)


# async def scheduled(delay):
#   await check_new_posts()

