from aiogram import types

from create_bot import vk_parser, mongo, bot

# Функция делает проверку на новый пост
def is_new_post_vk(post_id, last_post_id):
  return str(post_id) != str(last_post_id)


# Функция отправляет сообщение в канал
async def send_message_from_vk(channel_id, post):
  try:
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
          
        elif attachment['type'] == 'video':
          video_url = vk_parser.get_video_url(attachment)

          print(video_url)

        print(attachment)

        flag = False

      # Если длина сообщения больше 4096
      if len(post['text']) > 1024: 
        for x in range(0, len(post['text']), 4096):
          await bot.send_message(channel_id, post['text'][x:x+4096])


      # Если есть обработанные вложения
      if len(media.to_python()):
        await bot.send_media_group(channel_id, media=media)
      
      print('Post has been deployed')
  except Exception as e:
    print(e)


# Функция получает новый пост и записывает его id как lastkey в БД
def get_last_post_vk(user_id, public_id):
  post = vk_parser.get_last_post(public_id)
  post_id = str(post['id'])

  mongo.update_vk_public_lastkey(user_id, public_id, post_id)

  return post
