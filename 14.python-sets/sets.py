# Create a set of characters
sonic_characters = {
  "Doctor Eggman",
  "Shadow",
  "Knuckles",
  "Sonic",
}

print(sonic_characters)

# Iterate over the set of items
# using a for loop

for sonic_character in sonic_characters:
  print(sonic_character)

# Check for membership for a specific character in our set

print("Batman" in sonic_characters)


# add method - To add a item to our set
# update method - To add one or more items to our set

# Define a set of unique IDs
ids_set = {
  "i01",
  "i02",
  "i03",
  "i04"
}
# Add a new id to our set of IDs
ids_set.add("i05")
print(ids_set)

# To add multiple IDs to our set
ids_set.update(["i06", "i07", "i08"])
print(ids_set)

# To remove an item from our set, we can use
# remove method

# Remove the id of i01 from the set
ids_set.remove("i01")
print(ids_set)

# Using remove method if you try to remove an id that does
# does not exist in our set of IDs, the operation will error
# out
ids_set.remove('i09')

# For this case, we can use discard method on our set
# If the id that you are trying to delete is present
# in the set, it will delete that otherwise it will
# not raise any error and the original set gets printed

ids_set.discard("i09")
print(ids_set)

# Pop method can be used to remove last item from out set
# though it is unreliable because each time the order of elements
# is different and that means last item will be different
# each time the method gets executed
popped_item = ids_set.pop()
print(popped_item)
print(ids_set)

# To empty the complete set
ids_set.clear()

# To erase the existence of our set, we can use del keyword
del ids_set
