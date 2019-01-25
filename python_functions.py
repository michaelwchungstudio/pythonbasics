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
# small anonymous function, can take any number of arguments, but can only have one expression
# lambda arguments : expression
tlam = lambda a, b, c : a + b + c
print(tlam(1, 2, 3))
# mostly used as an anonymous function inside another function
def mult_func(n):
    return lambda a : a * n
doubler = mult_func(2)
tripler = mult_func(3)
print(doubler(11)) # prints 22
print(tripler(11)) # prints 33