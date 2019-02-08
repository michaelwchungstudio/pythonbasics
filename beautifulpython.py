## Transforming code into beautiful, idiomatic Python
# --------------
## Looping over a range of numbers
for i in range(6):
    print(i**2)

## Looping over a collection
colors = ['red', 'green', 'blue', 'yellow']

for color in colors:
    print(color)

## Looping backwards
for color in reversed(colors):
    print(color)

## Looping over a collection and indicies
for i, color in enumerate(colors):
    print(i, '-->', color)

## Looping over two collections
names = ['michael', 'john', 'matthew']

for name, color in izip(names, colors):
    print(name, '-->', color)

## Looping in sorted order
for color in sorted(colors):
    print(color)

for color in sorted(colors, reverse=True):
    print(color)

## Custom sort order
print(sorted(colors, key=len))

## Call a function until a sentinel value
blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

## Distinguishing multiple exit points in loops
# 'else' in for loops
# Two ways to exit this loop: 1) finish the loop, 2) break out
# If the value is never equal to the target, proceeds to 'else' and returns -1
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

# --------------
## Dictionary skills
# Fundamental tool for expressing relationships, linking, counting, and grouping

## Looping over dictionary keys
fav_color_dict = {'mike': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in fav_color_dict:
    print(k)

## Looping over dictionary keys, AND mutating it
# ** Try not to mutate something that you are iterating over! **
# In this case, .keys() creates a copy list of the keys
for k in fav_color_dict.keys():
    if k.startswith('r'):
        del fav_color_dict[k]

d = {k : fav_color_dict[k] for k in fav_color_dict if not k.startswith('r')}

## Looping over a dictionary keys and values
for k, v in fav_color_dict.items():
    print(k, '-->', v)

for k, v in fav_color_dict.iteritems():
    print(k, '-->', v)

## Construct a dictionary from pairs
names = ['mike', 'mochi', 'caroline']
colors = ['green', 'red', 'blue']

d = dict(izip(names, colors))
# {'mike': 'green', 'mochi': 'red', 'caroline': 'blue'}

d2 = dict(enumerate(names))
# {0: 'mike', 1: 'mochi', 2: 'caroline'}

## Counting with dictionaries
duplicate_colors = ['red', 'green', 'red', 'green', 'blue', 'red', 'green']

d = {}
for color in duplicate_colors:
    if color in d:
        d[color] += 1
    else:
        d[color] = 1
# {'blue': 1, 'green': 3, 'red': 3}

d = {}
for color in duplicate_colors:
    d[color] = d.get(color, 0) + 1

# defaultdict can easily be used to group a sequence of key-value pairs into a dictionary of lists
# defaultdict can also be useful for counting
# the parameter indicates what type the default value will be assigned if the key does not currently exist
from collections import defaultdict
d = defaultdict(int)
for color in duplicate_colors:
    d[color] += 1

s = 'mississippi'
d = defaultdict(int)
for letter in s:
    d[letter] += 1
d.items()
# [('i', 4), ('p', 2), ('s', 4), ('m', 1)]

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
d.items()
# [('blue', [2, 4], ('red', [1]), ('yellow', [1, 3]))]

## Grouping with dictionaries - Part I
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
# {5: ['roger', 'betty'], 6: ['rachel', 'judith'], 7: ['raymond', 'matthew', 'melissa', 'charlie']}






















#
