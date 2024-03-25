# Define a dictionary and a list with some values
d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']
d2 = {
    7:  "lucky seven",
    10: "ten",
    3:  "this is the new three",
}

# Creating a dictionary with keys specified in the iterable passed to the from_keys() method
# Also passing a default value of 0 to the dictionary
new_dict = dict.fromkeys(pantry_items, 0)
print(new_dict)

# The keys method can be used to iterate over the keys
# Not much used anymore, but can for example be used to make it clear what is being iterated over
print()
for item in d.keys():
    print(item)

# Using the update() method to update the value of the d2 dictionary
# Update the value for two keys, and insert one new key
# As we can see, updating the value of a key does not change the position of the key
# This is what the documentation means by the insertion order being preserved
print()
d.update(d2)
for key, value in d.items():
    print(key, value)

# Seeing how updating the d dictionary with the pantry_items will affect the output
# The first five items have been replaced with the values from the pantry dictionary
print()
d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key, value)

# The values() method is similar to the keys method, where it returns a list of values
print()
values = d.values()
print(values)

# Values cna be useful to check if a value exists in a dictionary, as seen below
# However, dictionaries are generally intended to be accessed via their keys
print()
print("egg" in values)
print("eleven" in values)

# Above, we see that egg exists in the dictionary, but do not know what they key is
# A way around that, to find the key, is by converting both the keys and values to lists
print()
keys = list(d.keys())
new_values = list(values)
if "egg" in new_values:
    index = new_values.index("egg")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

# A more efficient approach could be to loop through the dictionary items
# This approach would also return all results, if the value was present more than once
print()
for key, value in d.items():
    if value == "egg":
        print(f"{d[key]} was found with the key {key}")
