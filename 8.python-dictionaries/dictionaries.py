
# Dictionary
person = {
  "name": "Alex",
  "age": 21,
  "hobbies": ["Gardening","Coding"],
  "is_gamer": True,
  "address": {
    "street": "XYZ Street",
    "location": "XYZ"
  }
}
# name of the person (accessing an item of the dictionary)
print(person["name"])
print(person["age"])
print(person["hobbies"])

print(person["address"]["street"])

person["age"] = 22
print(person)

# Checking for membership
print("age" in person)

print(len(person))

# Adding a key-value pair to our dictionary
person["address"]["city"] = "City of XYZ"

print(person)

# Removing items from our dictionary

person.pop("age")
print(person)

# Remove the last inserted item of the dictionary
person.popitem()
print(person)

# Empty the entire dictionary
person.clear()
print(person)

