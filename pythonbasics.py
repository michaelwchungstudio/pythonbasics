# Python Basics

# Variables
# - cannot have spaces or symbols other than an underscore (_)
# - cannot begin with numbers, but can have numbers after the first letter (e.g. var_1)
# - variables are created the moment you first assign a value to it
# - variables can also change type after being initially set
breakfast = "steak and eggs"

# Strings
print("This is a string.")
# String concatenation
print("String 1" + "String 2")
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

# Numbers
# Integers
integer_example = 12
# Floats
float_example_one = 8.7
float_example_two = 35e3
float_example_three = -87.7e100
# Complex
complex_example_one = 3 + 5j
complex_example_two = 5j

# Casting - specifying a variable type
# 1. int() - constructs an integer from an integer literal, a float literal (rounds down), or a string (providing the string represents a whole number)
# 2. float()
# 3. str()

# Arithmetic (+, -, *, /)

# Exponents (**)
# 2 to the 10th power
print (2 ** 10)

# Plus Equals
number_of_miles = 12
number_of_miles += 2
print(number_of_miles)

# Errors
# - Python will point to error location with a ^ character
# - 1. SyntaxError: something is wrong with the way it is written (wrong punctuation, wrong command, missing parenthesis)
# - 2. NameError: code contains something that is a variable but was never defined