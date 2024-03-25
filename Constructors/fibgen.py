# Defining a function that will generate fibonacci numbers
def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


# Creating a variable for the function
fib = fibonacci()

# Printing the next value for the function, as it is infinite
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
