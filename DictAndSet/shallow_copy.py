# Defining a dictionary, to create a shallow copy
animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# This will print "toy", since both "things" and "animals" are referring to the same dictionary
# things = animals
# animals["teddy"] = "toy"
# print(things["teddy"])

# Creating a separate copy, using the copy() method to create a new dictionary
# With immutable objects, it does not matter if a copy is shallow or deep though
# print()
# things = animals.copy()
# animals["teddy"] = "toy"
# print(things["teddy"])

# With a shallow copy, the outputs will be the same, as the code is referring to the same list
# A shallow copy gives two dictionaries, but there are still only the three same lists
print()
things = animals.copy()
print(things["teddy"])
print(animals["teddy"])

# Showing how there are only the same three lists being used
# Toy is appended in both dictionaries, because we are working with a shallow copy
# The dictionary list in "animals" are stored in memory somewhere, and referenced by value
print()
things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
