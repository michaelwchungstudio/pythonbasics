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
if a > b or a > c:
    print("At least one is true :o")

## While loops
# A 'break' statement can be added to force-stop the loop when a condition is met
i = 1
while i < 6: # this loop will print numbers 1, 2, breaking once i = 3
    print(i)
    if i == 3:
        break
    i += 1
# A 'continue' statement can stop the current iteration and continue with the next
u = 0
while u < 6: # this loop will print numbers 1, 2, 4, 5, 6
    u += 1
    if i == 3:
        continue
    print(i)

## For loops
for x in "banana": # prints each character in the string 'banana'
    print(x)
# For loops can use 'break' and 'continue' statements in the same manner as while loops
fruits = ["apple", "kiwi", "mango"]
for x in fruits: # prints each fruit except 'kiwi'
    if x == "kiwi":
        continue
    print(x)
# range() function, returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at the specified number
for x in range(6): # this prints numbers 0 to 5, NOT including 6
    print(x)
 # range(startnumber, endnumbernotincl, increments)
for x in range(2, 30, 3):
    print(x)
# The 'else' keyword in a for loop specifies a block of code to be executed when the loop has finished
for x in range(6):
    print(x)
else:
    print("For loop is done!")
# Nested for loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)