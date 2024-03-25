# This is NOT a valid way to create an empty set
# Python has no way of knowing whether this is an empty set or an empty dictionary
# This code will create an empty dictionary, as seen below
numbers = {}
print(numbers, type(numbers))

# There is a way to create an empty set, using a literal, but it is not very elegant or much used
# The *"" expression represents unpacking applied to an empty string
# Unpacking an empty string results in no elements to unpack,  which effectively creates an empty set
numbers = {*""}
print(numbers, type(numbers))   

# This is a more commonly used way to create an empty set
numbers = set()
print(numbers, type(numbers))

# Items can be added to a set using the add() method
numbers.add(1)
print(numbers)

# Sets cannot contain duplicates, which can be useful if you for example want a user to add four unique numbers
# This code will keep looping if duplicate numbers are added to the numbers set
while len(numbers) < 4:
    next_value = int(input("Please add a new, unique number: "))
    numbers.add(next_value)
print(numbers)

# Creating a new list to see how this will work along with sets
data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list, to remove duplicates
# However, since sets are unordered, this code will output a list
# As such, when any data needs to be sorted, sets are automatically disqualified
unique_data = sorted(set(data))
print(unique_data)

# Create a list of unique colours, keeping the order they appeared
# Creating a dictionary using the fromkeys() method will preserve the order
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))

# Initialising a new set using the set function, to work on removing items from a set
# This set will print out in order, but it is still an unordered collection of items
small_ints = set(range(21))
print(small_ints)

# Removing all items from a set using the clear() method, which would result in an empty set
# small_ints.clear()
# print(small_ints)

# To delete individual items from a set, both the remove() and discard() methods can be used
# The only difference is that remove will raise an exception if the item is not present
small_ints.discard(10)
small_ints.remove(11)
small_ints.discard(99)
# small_ints.remove(99) # Raises an error, crashing the program
print(small_ints)
