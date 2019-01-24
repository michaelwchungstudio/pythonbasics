# Python Collections

# 1. List is a collection which is ordered and changeable. Allows duplicate members.
# 2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3. Set is a collection which is unordered and unindexed. No duplicate members.
# 4. Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

## Lists
thislist = ["eggs", "bacon", "coffee"]
print(thislist)
# The list() constructor
construct_list = list(("apple", "banana", "orange"))
print(construct_list)
# Access list items
print(thislist[1]) # prints 'bacon'
# Changing list item value
thislist[1] = "toast"
print(thislist) # prints ['eggs', 'toast', 'coffee']
# Looping through a list
for breakfast_item in thislist:
    print(breakfast_item)
# Check if item exists
if "eggs" in thislist:
    print("Yes, 'eggs' is in this list!")
# List length
print(len(thislist)) # prints 3
# Add item
thislist.append("orange")
# Add item at specified index
thislist.insert(1, "muffin")
# Remove item
# remove()
thislist.remove("eggs") # removes 'eggs', shifts items down an index position
# pop(), removes at specified index or the last item if index is not specified, can assign to another variable
breakfast_item_example = thislist.pop(1) # removes 'toast', item in position '1'
# del, removes specified index or can remove an entire list
del thislist[1] # removes 'coffee'
print(thislist) # thislist currently ['muffin', 'orange']
del thislist #thislist is deleted
# clear, empties a list
numlist = [1, 2, 3]
numlist.clear()
print(numlist) # prints []
## Other methods
# index(), search list for value and return first index where it is found
# copy(), returns a copy of the list
# extend(), add the elements of a list (or any iterable), to the end of a list
# sort(), sort a list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort() # sorts into ['BMW', 'Ford', 'Volvo']
cars.sort(reverse=True) # sorts into ['Volvo', 'Ford', 'BMW']
cars = ['Mitsubishi', 'BMW', 'VW']
def myFunc(e):
    return len(e)
cars.sort(key=myFunc) # sorts into ['VW', 'BMW', 'Mitsubishi']

## Tuples
thistuple = ("Thing 1", "Thing 2", "Thing 3")
# Accessing items, looping through, and checking if items exist in a tuple are the same as lists
# The values in a tuple CANNOT be changed!
# A value CANNOT be added to a tuple!
# A value in a tuple CANNOT be removed!
# del, can remove an entire tuple
del thistuple
## Other methods
# count(), returns number of instances a value occurs in a tuple

## Sets
thisset = {""}