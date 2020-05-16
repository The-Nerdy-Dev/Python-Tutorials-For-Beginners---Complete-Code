file_object = open("content.txt", mode="r", encoding="utf-8")

print(file_object)

content = file_object.read()
print(content)

# Current Cursor Position
print(file_object.tell())

# Changing the file cursor to a specific position
file_object.seek(23)

# Current Cursor Position
print(file_object.tell())

# Reading the file
for line in file_object:
  print(line,end="")

# Placing the cursor at the start of the file
file_object.seek(0)

# Reading the file
for line in file_object:
  print(line, end="")

# Placing the cursor at the start of the file
file_object.seek(0)

print(file_object.readline())

print(file_object.readlines())

# Manually closing the file
file_object.close()

# Writing content to a file

with open("quotes.txt", "w", encoding="utf-8") as file_object:
  file_object.write("Humility is the centrestone of excellence\n")
