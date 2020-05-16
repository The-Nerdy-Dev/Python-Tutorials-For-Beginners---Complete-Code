# Code for Functions 

def subscribe():
  print("You are subscribed to the channel")

subscribe()

# Passing parameters to our simple calculator function

def calculator(number_one, operator, number_two):
  if operator == '+':
    # print(number_one + number_two)
    return number_one + number_two
  elif operator == '-':
    # print(number_one - number_two)
    return number_one - number_two
  elif operator == '*':
    # print(number_one * number_two)
    return number_one * number_two
  elif operator == '/':
    # print(number_one / number_two)
    return number_one / number_two
  elif operator == '%':
    # print(number_one % number_two)
    return number_one % number_two
  elif operator == '**':
    # print(number_one ** number_two)
    return number_one ** number_two
  else:
    # print("Invalid operator")
    return "Invalid Operator"

result = calculator(8,'*',2)
print(result)


# *args and **kwargs

def subscription(*args):
  print(args)
  print(len(args))
  print(args[0] + " " + args[1] + " " + args[2] + " " +
  args[3] + " " + args[4])

subscription("XYZ","Subscribed","To","The","Channel")

# If
# the number of arguments
# is not known to you, just add an asterisk right
# before the parameter
# name.

# *kwargs
# Keyword argument is just a key-value pair with a key
# having a value

def do_some_thing(name, *args, **kwargs):
  print(name)
  print(args[0])
  sentence = ''
  for word in args[0]:
    sentence += " " + word
  print(sentence)
  print(args[1])
  print(kwargs)
  for game_prop,game_value in kwargs.items():
    print(game_prop, game_value)

do_some_thing("The World of Nerds",["Programming","is","easy"]
, "I am a useless argument", game="Counter Strike", rating=5,
is_favorite=True)

# Pass Statement

# So I will say
def some_complex_function():
  pass

some_complex_function()
