## Python modules
# equivalent to a code library
# file containing a set of functions you want to include in your application
# modules can be created by saving code into a file with the extension .py
# modules can contain functions but also variables of all types (arrays, dictionaries, objects, etc.)
# you can create an alias when importing a module, by using the 'as' keyword

## Using/importing a module
import examplemodule as exmod

exmod.greeting("Michael") # prints 'Hello, Michael'
print(exmod.person1["name"]) # prints 'Michael'
print(exmod.person1["age"]) # prints '26'
print(exmod.person1["country"]) # prints 'USA'

## Importing specifics of a module, use the 'from' keyword
from examplemodule2 import car1
print("I drive a " + str(car1["year"]) + " " + car1["company"] + " " + car1["model"] + ".")

## Built-in modules
# https://docs.python.org/3/py-modindex.html
import platform
plat = platform.system()
print(plat)

## dir() function
# built-in function to list all the function or variable names in a module
print(dir(platform))

