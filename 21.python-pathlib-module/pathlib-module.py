from pathlib import Path

# Setup a path first
path = Path("hello.py")
print(path)

# To get the home directory of the
# current user
print(path.home())
print(path.exists())


# To check whether the path represents a path
# to file
print(path.is_file())
# To check whether the path represents a path
# to the directory
print(path.is_dir())
# To get the suffix of the path
print(path.suffix)  # extension of the file

# To get the the name of the file on which the path is setup
# without the suffix
print(path.stem)

# The parent of the file
# on which we set up the path object
print(path.parent)

#  absolute path for the file hello.py
print(path.absolute())
