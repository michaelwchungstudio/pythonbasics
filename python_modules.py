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


