# Hey guys I am back with a new video
# So in this video we will learn about
# the operators that we can make use of
# in Python

# So we have seven types of operators and we will
# go over all of them in this video.

# So first is arithmetic operators
# Arithmetic operators are those operators
# that are used with numerical values to perform
# some common mathematical arithmetic operations

# So we have addition
a = 3
b = 2
print(a + b) # Addition
print(a-b)  # Subtraction
print(a*b)  # Multiplication
print(a/b)  # Division
print(a % b) # Modulus
print(a**b)  #Exponentiation
print(a//b)  # Floor Division

# Let us move forward to assignment
# operators
# These operators are used to assign values
# to variables

# So first is the normal equal to
x = 7  # Here we are assigning x to 5
x += 2  # This is equivalent to adding 3 to x and then
# storing the result that you get back to x
# which means x+=3 is same as x = x + 3
# Then I can say
x -= 5
x *= 8
x /= 3
x %= 2
x **= 4 # Exponentiation

# Now let us understand about the comparision
# operators and this you will mostly find being used
# in conditional checks which we will discuss later.

print(3 == 2) # Equal to
print(3 != 2) # Not equal
print(3 > 2)  # Greater than
print(5 < 3)  # Less than
print(4 >= 4) # Greater or equal to
print(4 > 4)
print(3 <= 4) # Less than or equal to
print(3 <= 3)

# So now let us move forward to logical operators
# in Python

# These are those operators that are used to combine
# conditional statements

# So we have and, or and not logical operators
print(3 < 2 and 3 > 1)
print(2 < 3 or 5 < 3)
print(not (2 < 3 and 5 > 2))

# Then we have the identity operators
# Identity operators are used to compare the
# references whether they point to the exact same object
# that is they share the same memory location or are different
# objects.

# Returns true if both of the
# things being compared are the same
# objects
print([1, 2, 3] is [1, 2, 3])
# Returns true if both the variables are
# not the same objects
print([1,2,3] is not [1,2])

# So now let us discuss about the
# membership operators
# Membership operator is used to check whether
# a thing is present in an object or not
# So if I say
print(1 in [1, 2, 3])
# in here returns true if 1 is present in
# the given list of values

print(7 not in [1, 2, 3])
# not in returns true if  7 is not present
# in the given list of values

# So finally let us go over the bitwise operators
# So bitwise operators are used to compare binary numbers

# So we have bitwise AND, bitwise OR, bitwise XOR,
# bitwise NOT, Left Shift Operator and Right Shift Operator

number_one = 8 # It is 1000 in binary
number_two = 5 # It is 0101 in binary

# So first let us perform the bitwise AND operator on
# our numbers
print(number_one & number_two)  # 0 which is 0000 in binary
# So let us perform bitwise OR operator on our given numbers
print(number_one | number_two)  # 13 which is 1101 in binary

# So now comes the bitwise XOR operator. In case of this if the
# corresponding bits of both the numbers are same, then it is 0
# else
# it is 1 so let us apply this rule to understand what we get
print(number_one ^ number_two) # So here also we get 13
# which is 1101 in binary

# Then we have bitwise NOT
# So this returns 1's compliment of a number
number_three = 10
print(~number_three)
# So if we have a number 1000 then you will take its

# ~a = ~1010
#    = -(1010 + 1)
#    = -(1011)
#    = -11 (Decimal)

# Now coming to the final type of operators that I want to cover
# are the shift operators
# These operators are used to shift the bits of a
# number left or right thereby multiplying or
# dividing the number by two respectively.
# They can be used when we have to multiply
# or divide a number by two.

# Let us first understand about bitwise right shift

# It Shifts the bits
# of the number to the right and
# fills the vacant spaces that we get as a result with 0
# It is equivalent to dividing the number with some power
# of 2

# So let us consider an example:

# Example 1:
# g = 10
# g >> 1 = 5

# Example 2:
# h = -10
# h >> 1 = -5


# It Shifts the bits
# of the number to the left and
# fills the vacant spaces that we get as a result with 0
# It is equivalent to multiplying the number with some power
# of 2

# Let us see an example on left shift now :

# g = 5 = 0000 0101
# h = -10 = 1111 0110

# g << 1 = 0000 1010 = 10
# g << 2 = 0001 0100 = 20

# h << 1 = 0000 1010 = -20
# h << 2 = 0001 0100 = -40

# So this was all about the video on Operators.
# So if you liked the video, do give it a thumbsup,
# subscribe to the channel,
# hit the bell icon for all the upcoming uploads,
# and I will see you guys next time.
