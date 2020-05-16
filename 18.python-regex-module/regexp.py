import re
channel_name = "The Nerdy Dev"

# search method
matched_portion = re.search("^The.*Dev$", channel_name)



# METACHARACTERS [To learn more about metacharacters
# check out the Python official docs]
# ^ - means that the string under check should start with The
# * means zero or more regular occurrences
# .  means any character except the newline character
# * 0 or more occurrences of any character are allowed
# $ - string under check should end with Dev.

# findall method to get the list of all the matches

description = """
It is a very juicy, pulpy and luscious fruit.
Ripe mangoes can either be consumed raw or in the form of
salad,
juice, jams, milkshake or pickles.
Mango is a rich source of various vitamins and minerals.
It is regarded as the king of fruits and comes in various
shapes and sizes.
Mango is my favourite fruit because it has a
sweet and refreshing flavour.
In addition to its taste, the fruit has many
nutritional and health benefits too.
Mango is a tasty fruit and everyone loves its
juicy and lip-smacking flavour.
"""

matches = re.findall("be",description)
print(matches)
first_whitespace = re.search("\s", description)
print(first_whitespace.start())
# To find the first whitespace character
# \s is a special sequence
# To learn more on special sequences check out the
# Python official docs


# split method to split the string
# into a list of words at some specific
# symbol or character
result = re.split('\s', description)
print(result)

# sub method
# Used to
# replace the matches with the text
# of your choice

# Let us remove whitespace character with
# * in our description string
text = re.sub("\s", "*", description)
print(text)

# Email validation example

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def validateEmail(email):
    if(re.search(regex,email)):
        print("The given email is a valid one.")
    else:
        print("The given email is an invalid one.")
email = "nerdsworld@gmail.com"
validateEmail(email)

email = "xyz.com"
validateEmail(email)

random = "I am not an email"
validateEmail(random)

