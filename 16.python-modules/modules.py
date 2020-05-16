# Working with core module of Python Library
import math

print(math.sqrt(87))

# Import our own created games module
import games

# Access the functionality from that module
# that we just imported

print(games.favorite_games)

# Second way of importing a certain
# functionality from a module

from games import play_game

play_game()
