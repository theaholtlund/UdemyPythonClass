# Define some lists to work on
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Some common sequence operations
print(min(even)) # Minimum value
print(max(odd)) # Maximum value
print(len(even)) # Number of items in the sequence
print(len(odd)) # Number of items in the sequence
print("Mississippi".count("s")) # Number of times the character appears

# Using the sort method, this does not create a copy, just rearranges it
even.extend(odd)
print(even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)

# Sorting with letters, capital letters are sorted first
pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)

# Sorting with floating point numbers
# Sorted() returns a new list, while .sort() modifies the original list
numbers = [2.3, 4.5, 6.7, 3.1, 9.2, 1.6]
numbers.sort()
print(numbers)

# Sorting with caseless string comparison, using casefold() method
names = ["Graham", "eric", "John", "adam", "Michael", "Bob"]
names.sort(key=str.casefold)
print(names)
