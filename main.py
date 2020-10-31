import json
from user import User

secretSantaList = []

with open('./data.json') as data:
  userData = json.load(data)
  for user in userData:
    secretSantaList.append(User(user['name'], user['email']))

  for user in secretSantaList:
    print(user.name)
    print(user.email)
