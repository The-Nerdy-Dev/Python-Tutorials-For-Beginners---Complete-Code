def square(number):
  return number**2

# SYNTAX : lambda arguments: expression
# An equivalent lambda for above function
square_lambda_version = lambda number: number ** 2
print(square_lambda_version(9))

# Also if you print
print(square.__name__)
print(square_lambda_version.__name__)
