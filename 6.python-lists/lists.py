
# Lists

programming_languages = ['Python','JavaScript','C++','Java']

messed_up_list = [
  "I love football",
  4.5634,
  True,
  {
    'name': 'Alexander',
    'age': 21,
     "books": ["X","Y"]
  },
  ["Anything","Does not matter"]
]
print(programming_languages)
print(messed_up_list)

# Finding the length of the list
print(len(programming_languages))
print(len(messed_up_list))

# Accessing the element using indexing
print(programming_languages[0])
print(programming_languages[3])

# Changing items in a list
messed_up_list[0] = "Changed"
print(messed_up_list)

print(programming_languages[len(programming_languages)-1])

# Negative indexing

print(programming_languages[-1])

# Range Selection
# [start_index:end_index]

# Printing the first three languages of our list
print(programming_languages[0:3])

# All the languages starting from index 1
print(programming_languages[1:])

# First three languages using negative range selection

print(programming_languages[-4:-1])

# Checking for membership
print("Cobol" in programming_languages)

# Adding items to the list
# Adding an item to the end of the list
programming_languages.append("Ruby")
print(programming_languages)

# Adding an item at a specific index
programming_languages.insert(1,"C")
print(programming_languages)

# Removing items from the list

programming_languages.remove("C")
print(programming_languages)

programming_languages.pop(2);
print(programming_languages)

programming_languages.pop()
print(programming_languages)
