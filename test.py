import vk_api
from config import VK_TOKEN

session = vk_api.VkApi(token=VK_TOKEN)
api = session.get_api()
api_version = 5.81


def get_last_post(owner_id):
  def check_is_pinned(post):
    return True if not post.get('is_pinned') else False

  posts = api.wall.get(owner_id=owner_id, count=2, v=api_version)['items']
  post = list(filter(check_is_pinned, posts))
 
  return post


print(get_last_post(-67580761))
