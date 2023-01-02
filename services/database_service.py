from pymongo import MongoClient

import config

class Database:
  def __init__(self, database_uri):
    # Подключаемся к БД
    self.client = MongoClient(database_uri)
    self.db = self.client['bot']
    self.users = self.db['users']

  def add_user(self, id, name):
    # Добавляем пользователя
    self.users.insert_one({
      "user_id": id,
      "name": name,
      "subscribe": True,
      "vk_parser": {
        "publics": [],
      },
      "inst_parser": {
        "publics": []
      },
      "tg_channels": []
    })

  def get_users(self):
    return self.users.find({})

  def get_user(self, id):
    return self.users.find_one({"user_id": id})


  def unsubscribe_user(self, id):
    self.users.update_one({"user_id": id}, {"$set": {"subscribe": False}})

  def subscribe_user(self, id):
    self.users.update_one({"user_id": id}, {"$set": {"subscribe": True}})

  def add_tg_channel(self, user_id, chanel_id):
    self.users.update_one({"user_id": user_id}, {"$push": {"tg_channels": chanel_id}})

  def add_vk_public(self, user_id, public_id):
    self.users.update_one({"user_id": user_id}, {"$push": {"tg_channels": public_id}})




