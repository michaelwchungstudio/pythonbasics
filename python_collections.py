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
## Other methods, https://www.w3schools.com/python/python_lists.asp
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
# The tuple() constructor
construct_tuple = tuple(["apple", "banana", "orange"])
# Accessing items, looping through, and checking if items exist in a tuple are the same as lists
# The values in a tuple CANNOT be changed!
# A value CANNOT be added to a tuple!
# A value in a tuple CANNOT be removed!
# del, can remove an entire tuple
del thistuple
## Other methods, https://www.w3schools.com/python/python_tuples.asp
# count(), returns number of instances a value occurs in a tuple

## Sets
thisset = {"PUBG", "Fortnite", "Call of Duty"}
# The set() constructor
construct_set = set(["apple", "banana", "orange"])
# Sets are UNORDERED, so the items will appear in a random order
# Cannot access items in a set by referring to an index
# Looping through and checking if items exist in a set are the same as lists and tuples
# Cannot change items in a set
# Add an item
thisset.add("Overwatch")
# Add multiple items
thisset.update(["Battlefield", "Guild Wars 2"])
# Remove an item
thisset.remove("Battlefield") # If the item does not exist, this will raise an error
thisset.discard("Overwatch") # If the item does not exist, this will NOT raise an error
qtest = thisset.pop() # Removes the last item; since sets are unordered, you will not know what item is removed
# Clearing and deleting is the same as list and tuples
# Other methods - check https://www.w3schools.com/python/python_sets.asp

## Dictionaries, has keys and values (similar to objects in JavaScript!)
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# The dict() constructor
thisdict = dict(brand="Ford", model="Mustang", year="1964") # note that the keywords are NOT string literals
# Access items, refer to the key, can use get()
print(thisdict["model"])
print(thisdict.get("model"))
# Change value of an item by referring to the key
thisdict["year"] = 2019
# Looping through a dictionary
# Accessing key names in a loop
for key in thisdict:
    print(key)
# Accessing values in a loop, can use values()
for key in thisdict:
    print(thisdict[key]) 
for value in thisdict.values():
    print(value)
# Accessing both keys and values using the items() function 
# Second loop uses f-strings, https://realpython.com/python-f-strings/
for x, y in thisdict.items():
    print(x, y)
for x, y in thisdict.items():
    print(f"{x}: {y}")
# Checking if an item exists is the same as a list
if "model" in thisdict:
    print("Yes, 'model' is one of the keys.")
# Adding items
thisdict["color"] = "red"
# Removing items
thisdict_model = thisdict.pop("model")
del thisdict["color"]
# Other methods, https://www.w3schools.com/python/python_dictionaries.asp