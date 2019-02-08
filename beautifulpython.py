## Transforming code into beautiful, idiomatic Python
# --------------
# Looping over a range of numbers
for i in range(6):
    print(i**2)

# Looping over a collection
colors = ['red', 'green', 'blue', 'yellow']

for color in colors:
    print(color)

# Looping backwards
for color in reversed(colors):
    print(color)

# Looping over a collection and indicies
for i, color in enumerate(colors):
    print(i, '-->', color)

# Looping over two collections
names = ['michael', 'john', 'matthew']

for name, color in izip(names, colors):
    print(name, '-->', color)

# Looping in sorted order
for color in sorted(colors):
    print(color)

for color in sorted(colors, reverse=True):
    print(color)

# Custom sort order
print(sorted(colors, key=len))

# Call a function until a sentinel value
blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

# Distinguishing multiple exit points in loops
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
# Dictionary skills
# Fundamental tool for expressing relationships, linking, counting, and grouping

# Looping over dictionary keys
fav_color_dict = {'mike': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in fav_color_dict:
    print(k)

# Looping over dictionary keys, AND mutating it
# ** Try not to mutate something that you are iterating over! **
# In this case, .keys() creates a copy list of the keys
for k in fav_color_dict.keys():
    if k.startswith('r'):
        del fav_color_dict[k]

d = {k : fav_color_dict[k] for k in fav_color_dict if not k.startswith('r')}

# Looping over a dictionary keys and values
for k, v in fav_color_dict.items():
    print(k, '-->', v)

for k, v in fav_color_dict.iteritems():
    print(k, '-->', v)

# Construct a dictionary from pairs
names = ['mike', 'mochi', 'caroline']
colors = ['green', 'red', 'blue']

d = dict(izip(names, colors))
# {'mike': 'green', 'mochi': 'red', 'caroline': 'blue'}

d2 = dict(enumerate(names))
# {0: 'mike', 1: 'mochi', 2: 'caroline'}

# Counting with dictionaries
duplicate_colors = ['red', 'green', 'red', 'green', 'blue', 'red', 'green']

d = {}
for color in duplicate_colors:
    if color in d:
        d[color] += 1
    else:
        d[color] = 1
# {'blue': 1, 'green': 3, 'red': 3}

















#
