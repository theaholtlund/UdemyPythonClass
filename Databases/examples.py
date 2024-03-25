# Working with exceptions and error handling
def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# Handling the exception occurring when the call stack overflows, for numbers that are too large
try:
    print(factorial(1000))
except (RecursionError, OverflowError):
    print("This program cannot calculate factorials that large")

print("Program terminating")
