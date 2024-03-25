# Working with list comprehension
# Print the path of the current script or module
print(__file__)

# Defining a list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# The general syntax for list comprehension is new_list = [expression for item in iterable if condition]
# Everything that applies to list comprehension also applies to set comprehension in this context
squares = [number ** 2 for number in range(1, 7)]

print(squares)
