# Dictionaries store values in a key, sort of like an address
# Dictionaries use curly braces:
d = {'Gabe': 8643845473,
     'Ben': 8643841612,
     'Joy': 8644945914}
# A dictionary named 'd' has been created with three elements.
# --------------------------------------------------
# Specific element values in a dictionary can be accessed by calling the key:
print(d['Gabe']) # Outputs 8643845473
# --------------------------------------------------
# New elements can be added to a dictionary by providing a new key and setting it to a value:
d['Glen'] = 8643507576
print(d)
# The new element has been added to the dictionary.
# --------------------------------------------------
# Elements can be deleted by using 'del':
del d['Glen']
print(d)
# Now the element has been removed from the dictionary.
# --------------------------------------------------
# Using 'for' and 'in', you can go through every element in a dictionary:
for key in d:
    print('Key:', key, '| Value:', d[key])
# This for loop prints every key and its value by using the 'in' statement.
# 'in' can also be used to check if a key exists in a dictionary:
if 'Gabe' in d:
    print(True)
else:
    print(False)

if 'Jessica' in d:
    print(True)
else:
    print(False)
# --------------------------------------------------
# You can clear a dictionary of all of its items by using the 'clear' function:
d.clear()
print(d)
# The dictionary has been emptied and no longer has any of its items (notified by the empty curly braces when the
# program prints d).

# --------------------------------------------------
# --------------------------------------------------

# Tuples are like lists, but unlike lists they cannot be changed (immutable).
# Tuples are also much faster than lists.
# Tuples use normal parentheses:
t = (5, 9)
# A tuple named 't' has been created with two values of 5 and 9.
# --------------------------------------------------
# A tuple's items can be accessed the same way a list's can, with index values:
print(t[0])
# --------------------------------------------------
# Lists are used when all of the items have a similar meaning, such as ingredients in a recipe (Homogeneous).
# Tuples are used when each of the items all have different meanings, like a point on a graph with an x and y coord
# (Heterogeneous).




