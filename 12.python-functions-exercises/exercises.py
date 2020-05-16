# Exercise-1
# Given a list of numbers, you have to find the sum of all
# the numbers

def get_total(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

result = get_total([1,2,3,4,5])
print(result)

# Exercise-2
# Given a list of products where each product is a dictionary
# let us compute the total bill amount given that tax on each
# product is 4% of the price of the product

# List of products
products = [
  {
    'name': 'Shoes',
    'price': 164.99,
  },
  {
    'name': 'Laptop',
    'price': 567.44,
  },
  {
    'name': 'TV',
    'price': 745.55
  },
  {
    'name': 'Nintendo 3DS',
    'price': 545.55
  }
]

def compute_bill(products):
  total = 0.0
  for product in products:
    total += (product["price"] + product["price"]*0.04)
  return total

bill_amount = compute_bill(products)

print(bill_amount)
