## Python iterators
# An iterator is an object that contains a countable number of values
# It can be iterated upon, meaning you can traverse through all the values
# Object which implements the iterator protocol, consisting of the methods __iter__() and __next__()

## Iterator vs. Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects
# These objects have an iter() method which is used to get an iterator
mytuple = ("apple", "banana", "cherry")
myiterator = iter(mytuple)
print(next(myiterator)) # prints 'apple'
print(next(myiterator)) # prints 'banana'
print(next(myiterator)) # prints 'cherry'
# For loops actually create an iterator object and executes the next() method for each loop

## Create an iterator
# To create an object/class as an iterator, you have to implement the methods ___iter___() and __next__() to your object
# __iter__() acts similar to __init__() -> you can do operators but must always return the iterator object itself
# __next__() also allows you to do operators, and must return the next item in the sequence
# To prevent an iteration from going forever, use the StopIteration statement
class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        if self.num <= 20:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration

numbers = MyNumbers()
numiter = iter(numbers)

for x in numiter:
    print(x)