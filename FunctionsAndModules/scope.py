# Defining a function to calculate the factorial
def fact(n):
    """ Calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


# Defining a new function, which would be the recursive equivalent
# With this function, any one call is not returned until the function that n is called returns
# Effectively, it is called until n <= 1, and then returns the n values up until the n parameter
def factorial(n):
    # n! can also be defined as n * (n - 1)!
    """ Calculate n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1) # Calls itself with the value of (n - 1), effectively resulting in n * (n - 1)!


# The result of a Fibonacci sequence can also be calculated using a recursive function
# Each successive Fibonacci number is obtained by adding the two previous numbers
# This will process pretty slow, because it has to call itself twice
def fib(n):
    """ F(n) = F(n - 1) + F(n - 2) """
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# Here, an iterative approach might be better, as it will execute faster
def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
        return result


# Using the function to find the factorials
for i in range(36):
    print(i, fibonacci(i))
