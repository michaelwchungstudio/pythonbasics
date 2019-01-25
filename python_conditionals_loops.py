# Python conditions, if statements, and loops

## Conditions
# ==, !=, <, <=, >, >=

## If, elif, else statement
a = 33
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Shorthand if
if a > b: print("a is greater than b")
# Shorthand if .. else
print("a is greater than b") if a > b else print("a is not greater than b")

## And (&& in JavaScript!)
a = 5, b = 4, c = 6
if a > b and c > a:
    print("c is greater than a, which is greater than b")

## Or (|| in JavaScript!)
if a > b or a > c
    print("At least one is true :o")

##