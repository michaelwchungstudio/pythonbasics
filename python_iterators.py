## Python iterators
# An iterator is an object that contains a countable number of values
# It can be iterated upon, meaning you can traverse through all the values
# Object which implements the iterator protocol, consisting of the methods __iter__() and __next__()

## Iterator vs. Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects
# These objects have an iter() method which is used to get an iterator
mytuple = ("apple", "banana", "cherry")
myiterator = iter(mytuple)