# Defining a function to calculate a given number in a Fibonacci sequences
# We also add a docstring to document the function
# We also add function annotation and type hints
def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n` values."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


# We can now use the function we defined in our code
for i in range(36):
    print(i, fibonacci(i))
