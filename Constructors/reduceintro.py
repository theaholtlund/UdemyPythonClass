# Import required modules
import timeit
import functools


# Defining a function to calculate the product of two numbers
def calc_values(x, y: int):
    return x * y


# Defining a list of numbers to work with
numbers = [2, 3, 5, 8, 13]

# Using the reduce() function to add the numbers using the calc_values() function
reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)
# print(sum(numbers))

# Accomplishing the same result using a for loop
result = 1
for x in numbers:
    result *= x
print(result)

# Accomplishing the same result iterating over the values manually through variables
result = calc_values(2, 3)
result = calc_values(result, 5)
result = calc_values(result, 8)
result = calc_values(result, 13)
print(result)
