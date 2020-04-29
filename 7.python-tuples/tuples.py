
# Tuples
colors = ("red", "green", "orange")

print(colors)
print(colors[1])

# Negative Indexing
print(colors[-1])

# Range selection
# To access the first two colors of our tuple
print(colors[0:2])

# Same using negative range selection
print(colors[-3:-1])

# colors[0] = "pink" Won't work

# Converting the tuple to a list
colors_list = list(colors)
colors_list[0] = "pink"

# Convert back our list to the original tuple
colors = tuple(colors_list)

print(colors)

# Checking membership of an element in a tuple
print("purple" in colors)

print(len(colors))
