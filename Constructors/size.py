# Importing required modules
import sys


# Defining a generator function where the yield statement is used to define a generator
# In other words, the created generator generates a sequence of numbers starting from 0 up to n-1
# Had we used return, the function would have just returned one value
# Yield does not just return the value, it also keeps track of all the variables
def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


# Big_range is a generator object, based on the my_range function
# Confirm when the code is executed by printing the line number
# Underscore as the variable name to indicate that we are not actually interested in the value of the variable
# _ = input("Line 19")
big_range = my_range(5)
# _ = input("Line 21")

# Next returns the next value from the generator
# This "consumes" the first value of the iterator, and the loop will then return 1 as the first value
print(next(big_range))
print("Big_range is {} bytes".format(sys.getsizeof(big_range)))

# Create a list containing all the values in big_range
big_list = []

# Big_range is called every time it is iterated over in the loop
# A for loop is just calling the next function for us
# _ = input("Line 30")
for val in big_range:
    # _ = input("Line 24, inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
