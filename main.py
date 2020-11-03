import json
import random
import secret_santa
import yagmail
from getpass import getpass
from user import User

secret_santa_list = []
players = []
show_selected_users = False
print('Starting Super Secret Santa!')
try:
  print('Attempting to find data')
  with open('./data.json') as data:
    user_data = json.load(data)
  print('We have discovered preexisting data with the following users.')

  for user in user_data:
    print(user['name'])

  print('Would you like to run super secret santa with these players?')
  possible_answers = ['y', 'n']
  continue_with_old_users = input("Please input y or n to continue: ")
  while continue_with_old_users not in possible_answers:
    continue_with_old_users = input("Unrecognized command, please enter y or n: ")

  print('Understood!')
  if continue_with_old_users == 'y':
    for user in user_data:
      secret_santa_list.append(User(user['name'], user['email']))
      players.append(user['name'])
  else:
    user_input = ""
    while True:
      user_input = input('Please enter each players first name and email separated by spaces.\nOnce you are done, please type done. \n')
      if user_input == 'done':
        break
      secret_santa_list.append(User(*user_input.split(' ')))
    print(secret_santa_list)
    for user in secret_santa_list:
      players.append(user.name)

    print('Success! We have created entries for the following players: ')
    for user in secret_santa_list:
      print(user.name +
            ' with the email ' +
            user.email)
    print('Would you like to overwrite your previous save file with the new users?')
    possible_answers = ['y', 'n']
    overwrite_save_data = input("Please input y or n to overwrite: ")
    while overwrite_save_data not in possible_answers:
      overwrite_save_data = input("Unrecognized command, please enter y or n: ")
    if overwrite_save_data == 'y':
      with open('./data.json') as save_data:
        save_data.write(secret_santa.serialize_users(secret_santa_list))

except FileNotFoundError:
  print('oopsie')



secret_santa.assign_users_their_secret_santas(secret_santa_list, players)

email = input('Please enter your gmail address: ')
password = getpass('Please enter your password: ')

yag = yagmail.SMTP(email, password)

# for user in secret_santa_list:
#   yag.send(user.email, 'Secret Santa Selected!', [
#       'Ho ho ho!',
#       'Be ready for the anxiety ridden shopping of buying something that you hope this person will like,',
#       'The person that was selected for you was ' + user.selected_secret_santa,
#       'Good luck! Remember I have no idea who was selected for you, it is deleted immediately for me aftewards.'
#   ])
