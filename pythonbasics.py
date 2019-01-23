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