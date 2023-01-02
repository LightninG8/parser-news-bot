from aiogram import types
import asyncio
import aioschedule

from create_bot import parser, bot, mongo
from utils import is_new_post

async def check_new_posts():
    users = mongo.get_users()

    for user in users:
      


















    # try:
      channel_id = '-1001724347904'
      post = parser.get_last_post()
      id = post.get('id')
    
      # Если новый пост
      if is_new_post(id, parser.lastkey):
        # print(post)

        # Обновляем id последнего поста
        parser.update_lastkey(id)

        # Отправляем сообщения
        # Если нет вложений
        if len(post['attachments']) == 0:
          for x in range(0, len(post['text']), 4096):
            await bot.send_message(channel_id, post['text'][x:x+4096])

        # Если есть вложения 
        else:
          media = types.MediaGroup()

          flag = True

          # Если длина сообщения больше 1024
          if len(post['text']) > 1024: 
            flag = False
    
          for attachment in post['attachments']:
            if attachment['type'] == 'photo':
              url = attachment['photo']['sizes'][-1]['url']
        
              # Добавляем caption только первому изображению
              if flag:
                media.attach_photo(url, caption=post['text'])
              else:
                media.attach_photo(url)
              
            # elif attachment['type'] == 'video':
            #   videos = parser.api.video.get(owner_id=attachment['video']['owner_id'], videos=f"{ attachment['video']['owner_id'] }_{attachment['video']['id']}_{attachment['video']['access_key']}")

            #   print(videos)

            print(attachment)

            flag = False




          # Если длина сообщения больше 4096
          print(len(post['text']))

          if len(post['text']) > 1024: 
            for x in range(0, len(post['text']), 4096):
              await bot.send_message(channel_id, post['text'][x:x+4096])


          # Если есть обработанные вложения
          if len(media.to_python()):
            await bot.send_media_group(channel_id, media=media)
          
          print('News has been posted')

          


  # except Exception as e:
    # print(str(e))


async def scheduled(delay):
  aioschedule.every(delay).seconds.do(check_new_posts)

  while True:
    await aioschedule.run_pending()
    await asyncio.sleep(1)
