# Defining a function to return odd numbers
def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2


# Defining a function to find the Leibniz formula for pi
def pi_series():
    odds = oddnumbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


# Setting a variable for the function
approx_pi = pi_series()

# Looping through to get closer to the actual value of pi
for x in range(1000000):
    print(next(approx_pi))
