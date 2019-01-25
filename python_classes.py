## Classes
# object constructor, "blueprint" for creating objects
# the __init__() function is called automatically every time the class is being used to create an object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print("Hello my name is " + self.name)

p1 = Person("Michael", 26)

# modify object properties
p1.age = 27
# delete object properties
del p1.age
# delete objects
del p1