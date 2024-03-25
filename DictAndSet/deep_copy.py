# Importing copy for deep copying and defining a dictionary, to create a deep copy
import copy
animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# With a deep copy, the outputs will not be the same, as the code is referring to different lists
# A deep copy gives two dictionaries, where the nested items are also copies
things = copy.deepcopy(animals)
print(things["teddy"])
print(animals["teddy"])

# Confirming that we have performed a deep copy by printing the ids of keys
print()
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])
