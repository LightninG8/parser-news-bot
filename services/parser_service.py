import os
import requests
from bs4 import BeautifulSoup as BS
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

class Parser:
  lastkey = ''
  lastkey_file = ''
  api_version = 5.81
  owner_id = -67580761

  def __init__(self, lastkey_file, token):
    self.lastkey_file = lastkey_file
    self.token = token
    
    self.session = vk_api.VkApi(token=self.token)
    self.api = self.session.get_api()

    if(os.path.exists(lastkey_file)):
      self.lastkey = open(lastkey_file, 'r').read()
    else:
      f = open(lastkey_file, 'w')
      self.lastkey = self.get_last_post(self)
      f.write(str(self.lastkey))
      f.close()

  def get_last_post(self):
    def check_is_pinned(post):
      return True if not post.get('is_pinned') else False

    posts = self.api.wall.get(owner_id=self.owner_id, count=2, v=self.api_version)['items']
    post = list(filter(check_is_pinned, posts))[0]
  
    return post

  def update_lastkey(self, new_key):
    self.lastkey = new_key

    with open(self.lastkey_file, "r+") as f:
      data = f.read()
      f.seek(0)
      f.write(str(new_key))
      f.truncate()



