
# SYNTAX of try-catch error handling mechanism (TRY/EXCEPT/FINALLY)
# try:
  # Do something
# except:
  # Error Handling

a = 27
try:
    b = a / 0
    print(b)
except ZeroDivisionError as e:
    print("ERROR: ", e)
finally:
    print("Everything done.")


def concatenate(string_one, string_two):
  try:
    print(string_one + string_two)
  except TypeError as te:
    print("Error occurred", te)

concatenate('the nerdy dev', 2)

# Handling multiple errors
# def divide(a, b):
#     try:
#       result = a / b
#       print(result)
#     except ZeroDivisionError as zde:
#       print("ERROR:", zde)
#     except TypeError as te:
#       print("Both a and b must be of same types and must be numbers",te)
#     else:
#       print("Division went well")


# print(divide(1,2))
print(divide(1,'the nerdy dev'))
print(divide(1,0))

# Let us improve the above function a bit

def divide(a, b):
    try:
      result = a / b
    except (ZeroDivisionError, TypeError) as error:
      print(error)
    else:
      print("Division went well")

name = "Alex"
# name = 1
if not type(name) is str:
  print("Name must be a string")

