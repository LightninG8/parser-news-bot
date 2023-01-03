import vk_api
import requests
from bs4 import BeautifulSoup as BS

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


# print(get_last_post(-67580761))

def get_video_url_vk(link):
  html = requests.get(link).text
  soup = BS(html, 'lxml')

  video_link = soup.find('div', id="page_wrap").find('source').get('src').split('?')[0]





  res = requests.get(video_link, stream=True)

  return video_link
  

print(get_video_url_vk('https://vk.com/video_ext.php?oid=-198932877&id=456239020&hash=56ea665d7b134d8d&__ref=vk.api&api_hash=167274972367e8610bf342d7f361_GIZTONBUGQ2DQMI'))
