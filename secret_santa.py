import random
import json

def assign_users_their_secret_santas(users, players):
  random.shuffle(users)
  random.shuffle(players)
  for user in users:
    selected_santa = user.name
    selected_player = random.choice(players)
    # Just incase the random player we selected was the same as the secret santa
    while selected_santa == selected_player:
      selected_player = random.choice(players)
    user.set_selected_secret_santa(selected_player)
    players.remove(selected_player)

def serialize_users(users):
  result = []
  for user in users:
    result.append({
      'name': user.name,
      'email': user.email
    })
  return json.dumps(result)
