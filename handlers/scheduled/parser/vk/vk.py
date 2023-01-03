from .utils import get_last_post_vk, is_new_post_vk, send_message_from_vk

async def parse_vk(user):
  user_id = user['user_id']

  for public in user['vk_parser']['publics']:
    public_id = public['id']
    lastkey = public['lastkey']

    post = get_last_post_vk(user_id, public_id)

    post_id = post['id']


    if is_new_post_vk(post_id, lastkey):

      for channel_id in user['tg_channels']:
        await send_message_from_vk(channel_id, post)
