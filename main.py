import json
import random
import secret_santa
import yagmail
from getpass import getpass
from user import User

secret_santa_list = []
players = []

with open('./data.json') as data:
  user_data = json.load(data)
  for user in user_data:
    secret_santa_list.append(User(user['name'], user['email']))
    players.append(user['name'])


secret_santa.assign_users_their_secret_santas(secret_santa_list, players)

email = input('Please enter your gmail address: ')
password = getpass('Please enter your password: ')

yag = yagmail.SMTP(email, password)

for user in secret_santa_list:
  yag.send(user.email, 'Secret Santa Selected!', [
      'Ho ho ho!',
      'Be ready for the anxiety ridden shopping of buying something that you hope this person will like,',
      'The person that was selected for you was ' + user.selected_secret_santa,
      'Good luck! Remember I have no idea who was selected for you, it is deleted immediately for me aftewards.'
  ])
