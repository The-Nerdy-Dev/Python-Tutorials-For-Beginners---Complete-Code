import random

favorite_games = [
  "Counter Strike",
  "The Witcher",
  "Need For Speed",
  "Call Of Duty"
]

def play_game():
  current_game = random.choice(favorite_games)
  print("I am playing", current_game)
