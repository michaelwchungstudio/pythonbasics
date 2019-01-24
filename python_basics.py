# Python Basics

## Variables
# - cannot have spaces or symbols other than an underscore (_)
# - cannot begin with numbers, but can have numbers after the first letter (e.g. var_1)
# - variables are created the moment you first assign a value to it
# - variables can also change type after being initially set
breakfast = "steak and eggs"

## Strings
print("This is a string.")
# String concatenation
print("String 1" + " " + "String 2")
# Multi-line strings
three_line_string = """
Line 1
    Line 2
Line 3
"""
# Strings are treated as an array of bytes representing unicode characters
# No character type, a single character is simply a string with a length of 1
a = "Hello, World!"
# Character of string
print(a[1])
# Substring
print(a[2:5])
# Additional functions:
# strip() removes whitespace from beginning or end
# len() returns the length of the string
print(len(a))
# lower() returns string in lower case
print(a.lower())
# upper() returns string in upper case
print(a.upper())
# replace() replaces a string with another string
print(a.replace("Hello", "Goodbye"))
# split() splits the string into substrings if it finds instances of the separator
print(a.split(","))
# Command-line string input
print("Enter your name:")
x = input()
print("Hello, " + x)

## Numbers
# Integers
integer_example = 12
# Floats
float_example_one = 8.7
float_example_two = 35e3
float_example_three = -87.7e100
# Complex
complex_example_one = 3 + 5j
complex_example_two = 5j

## Casting - specifying a variable type
# 1. int() - constructs an integer from an integer literal, a float literal (rounds down), or a string (providing the string represents a whole number)
# 2. float()
# 3. str()

## Arithmetic (+, -, *, /, %, // - floor division)

## Exponents (**)
# 2 to the 10th power
print (2 ** 10)

## Plus Equals
number_of_miles = 12
number_of_miles += 2
print(number_of_miles)

## Comparison operators (compare two values)
# ==, !=, >, <, >=, <=

## Logical operators (combine conditional statements)
# and, or, not
# and ex. x > 5 and x < 10
# or ex. x < 5 or x > 10
# not ex. not(x < 5 and x < 10)

## Identity operators (compare the objects, not if they are equal, but if they are the same object with the same memory location)
# is, is not

## Membership operators (test if sequence is present in an object)
# in, not in
x = ["apple", "banana", "strawberry"]
print("strawberry" not in x)  # returns false
print("strawberry" in x)  # returns true

## Bitwise operators
a_operator = 60  # in binary, 0011 1100
b_operator = 13  # in binary, 0000 1101
# & operator - AND
c_result = a & b  # if bit is shared, that bit remains -> if bit is different, defaults to 0
                  # &-ing returns 1 only if both bits are 1
                  # 0000 1100 => 12
# | operator - OR
c_result = a | b  # if either bit contains 1, resulting bit will equal 1
                  # |-ing returns 0 only if both bits are 0
                  # 0011 1101 => 61
# ^ operator - eXclusive OR
c_result = a ^ b  # returns 1 if one operand is 0 and another is 1, otherwise returns 0
                  # 0011 0001 => 49
# ~ operator - complement
c_result = ~a  # take each binary and return its complement
               # 1100 0011 => -61
# << operator - left shift operator
c_result = a << 2  # shift number of bits to left, x spaces
                   # 1111 0000 => 240
# >> operator - right shift operator
c_result = a >> 2  # shift number of bits to right, x spaces
                   # 0000 1111 => 15

## Errors
# - Python will point to error location with a ^ character
# - 1. SyntaxError: something is wrong with the way it is written (wrong punctuation, wrong command, missing parenthesis)
# - 2. NameError: code contains something that is a variable but was never defined