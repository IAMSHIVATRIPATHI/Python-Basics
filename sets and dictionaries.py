# Python Sets
# Sets are unordered collections of unique data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

# Example:
info = {"Carla", 19, False, 5.9, 19}
print(info)

# Creating an empty set
harry = set()
print(type(harry))

# Accessing set items using a for loop
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)

# Joining Sets
# Sets in python work similarly to sets in mathematics. We can perform operations like union and intersection on the sets.

# union() and update():
# The union() method returns a new set containing all items from both sets.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

# The update() method adds items from another set into the existing set.
cities.update(cities2)
print(cities)

# intersection() and intersection_update():
# The intersection() method returns a new set containing only items that are present in both sets.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

# The intersection_update() method updates the existing set with items that are present in both sets.
cities.intersection_update(cities2)
print(cities)

# symmetric_difference() and symmetric_difference_update():
# The symmetric_difference() method returns a new set containing items that are not present in both sets.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# The symmetric_difference_update() method updates the existing set with items that are not present in both sets.
cities.symmetric_difference_update(cities2)
print(cities)

# difference() and difference_update():
# The difference() method returns a new set containing items that are only present in the original set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

# The difference_update() method updates the existing set with items that are only present in the original set.
cities.difference_update(cities2)
print(cities)

# Set Methods
# isdisjoint():
# The isdisjoint() method checks if items of a given set are present in another set. It returns False if items are present, else it returns True.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities.issuperset(cities3))

# issubset():
# The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add()
# The add() method adds a single item to the set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# update()
# The update() method adds multiple items to the set.
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# remove() and discard()
# The remove() method removes the specified item from the set. If the item is not present, it raises a KeyError.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

# The discard() method removes the specified item from the set. If the item is not present, it does not raise an error.
cities.discard("Seoul")
print(cities)

# pop()
# The pop() method removes and returns an arbitrary item from the set.
item = cities.pop()
print(cities)
print(item)

# del
# The del keyword deletes the set entirely.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)  # This will raise a NameError as the set no longer exists.

# clear()
# The clear() method removes all items from the set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# Check if item exists
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")

# Python Dictionaries
# Dictionaries are ordered collections of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# Example:
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)

# Accessing Dictionary items:

# Accessing single values:
# Values in a dictionary can be accessed using keys.
print(info['name'])
print(info.get('eligible'))

# Accessing multiple values:
# The values() method returns a view object that displays a list of all the values in the dictionary.
print(info.values())

# Accessing keys:
# The keys() method returns a view object that displays a list of all the keys in the dictionary.
print(info.keys())

# Accessing key-value pairs:
# The items() method returns a view object that displays a list of dictionary's key-value tuple pairs.
print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

# Dictionary Methods

# update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
info.update({'age': 20})
info.update({'DOB': 2001})
print(info)

# Removing items from dictionary:

# clear()
# The clear() method removes all the items from the dictionary.
info.clear()
print(info)

# pop()
# The pop() method removes the key-value pair whose key is passed as a parameter.
info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.pop('eligible')
print(info)

# popitem()
# The popitem() method removes the last key-value pair from the dictionary.
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
info.popitem()
print(info)

# del
# The del keyword removes a dictionary item. If the key is not provided, it deletes the dictionary entirely.
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info['age']
print(info)

# If key is not provided, then the del keyword will delete the dictionary entirely.
del info
# print(info)  # This will raise a NameError as the dictionary no longer exists.

# Example usage of dictionary methods
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# Updating ep1 with ep2
ep1.update(ep2)
print(ep1)

# Clearing ep1
ep1.clear()
print(ep1)

# Popping an item from ep1
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep1.pop(122)
print(ep1)

# Popping the last item from ep1
ep1.popitem()
print(ep1)

# Deleting an item from ep1
del ep1[123]
print(ep1)
