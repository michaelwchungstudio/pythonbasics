## ...

## Python functions
# defined using 'def'
# parameters are specified inside the parentheses
def ex_function(fname):
    print("Hi, my name is " + fname)
ex_function("Michael")
# using default parameter values -> if the function is called without the parameter, it uses the default value
def country_function(fname, country = "USA"):
    print("My name is " + fname + " and I am from " + country)

country_function("Michael")
country_function("Angela", "China")
# use 'return' to let a function return a value
def mult_by_five(x):
    return 5 * x
print(mult_by_five(3))

## Recursive functions
def ex_recursion(x):
    if(x > 0):
        result = x + ex_recursion(x - 1)
        print(result)
    else:
        result = 0
    return result
ex_recursion(6) # prints 1, 3, 6, 10, 15, 21

## Lamba functions