
# JSON stands for JavaScript Object Notation
# and it is perfect for storing the data
# in the human readable format


# https://www.json.org/json-en.html


# 1. Converting JSON to something that Python Environment can
# recognize and that is a dictionary.

import json

person_json = '{"name": "Alex","age": 21,"hobbies":["Coding","Listening to Music","Gaming"] }'
# Parse the json using the loads method
person_dictionary = json.loads(person_json)
print(person_dictionary)

# Convert a dictionary into JSON

product_dict = {
  "id": "i01",
  "description": "An awesome pair of shoes made of fine leather",
  "price": 785.56
}
product_json = json.dumps(product_dict,
sort_keys=True
)
print(product_json)

# Convert a list to JSON
print(json.dumps(["orange", "red"]))
# A tuple to JSON
print(json.dumps(("orange", "red")))

# A number to JSON
print(json.dumps(31.76))

# A boolean to JSON
print(json.dumps(True))

# Reading from an external JSON file

from pathlib import Path

result = Path('persons.json').read_text()
print(result)

#Parse the JSON data that we get back
persons = json.loads(result)
print(persons)
