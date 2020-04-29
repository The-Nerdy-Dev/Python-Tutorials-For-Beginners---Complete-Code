
# Loops

for number in range(1,21):
  print(number)


answer = input("What is in my hand?")

while answer != "coins":
  print("You are wrong")
  answer = input("What is in my hand?")
print("You are right.")

# Iteration on lists, tuples and dictionaries

numbers = [1,2,3,4,5]

for number in numbers:
  print(number)

for index in range(len(numbers)):
  print(numbers[index])

# Iterating over the lists using the enumerate function

for (index,number) in enumerate(numbers):
  print(index,number)

# Dictionary iteration

# Iterating through all the keys

person_dict = {
  "name": "Alex",
  "age": 22,
  "hobbies": ["Gardening","Coding"],
  "address": {
    "street": "XYZ",
    "location": "XYZ"
  },
  "is_gamer": True
}

for person_detail_key in person_dict:
  print(person_detail_key)
# Iterating through all the values of the dictionary

for person_detail_value in person_dict.values():
  print(person_detail_value)

# Iterating through all the key value pairs of the dictionary

for (person_detail_key, person_detail_value) in person_dict.items():
  print(person_detail_key, person_detail_value)
