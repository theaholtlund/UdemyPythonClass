# Working with lambdas, which are anonymous functions
anon = lambda x: x * 2  # Not PEP 8 compliant


# Defining a function that does the same thing as the lambda expression
def double(x):
    return x * 2


# Confirming that the lambda expression and the function returns the same value
print(anon(7))
print(double(7))
