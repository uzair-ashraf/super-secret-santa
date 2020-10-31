import json
import random
import secret_santa
from user import User

secret_santa_list = []
players = []

with open('./data.json') as data:
  user_data = json.load(data)
  for user in user_data:
    secret_santa_list.append(User(user['name'], user['email']))
    players.append(user['name'])


secret_santa.assign_users_their_secret_santas(secret_santa_list, players)
