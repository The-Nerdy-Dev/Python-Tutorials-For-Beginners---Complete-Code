import os

# os.mkdir("d:\\nerds")

# os.chdir("d:\\nerds")
# print(os.getcwd())

# os.chdir("..")
# print(os.getcwd())

print(os.getcwd())
# os.mkdir("games")
try:
 os.rmdir("games")
except OSError as oe:
  print("OS Error", oe)
finally:
  print('Done.')

# Listing the files and directories of a specified directory
print(os.listdir("c:\\users"))
