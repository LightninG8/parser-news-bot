import vk_api
import requests
from bs4 import BeautifulSoup as BS

class VKParser:
  api_version = 5.81

  def __init__(self, token):
    self.token = token
    
    self.session = vk_api.VkApi(token=self.token)
    self.api = self.session.get_api()


  def get_last_post(self, owner_id):
    # Не учитываем посты в закрепе
    def check_is_pinned(post):
      return True if not post.get('is_pinned') else False

    posts = self.api.wall.get(owner_id=owner_id, count=2, v=self.api_version)['items']
    post = list(filter(check_is_pinned, posts))[0]
  
    return post

  def get_video_url(self, attachment):
    video = self.api.video.get(owner_id=attachment['video']['owner_id'], videos=f"{ attachment['video']['owner_id'] }_{attachment['video']['id']}_{attachment['video']['access_key']}")

    res = requests.get(video['player'])

    print(res)
    print(video)



