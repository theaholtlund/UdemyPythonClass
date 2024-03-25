# Pass a tuple to a function, by passing a sequence of values to bytes
# It is possible to use any iterable, as long as it produces integer values in the range 0 to 255
# The extra parenthesis indicates that it is a tuple, and not just five individual values
# equation = bytes((207, 128, 114, 194, 178))
equation = b'\xcf\x80r\xc2\xb2' # This is a bytes literal, and Python lets you create a literal bytes object like this
print(equation) # Outputs b'\xcf\x80r\xc2\xb2', default representation when printing a bytes object
print(type(equation)) # Outputs <class 'bytes'>, this confirms a bytes type
print(len(equation)) # Outputs 5, confirms that we have an array of bytes containing 5 values

# Checking the individual values in the array
for b in equation:
    print(b, end=', ') # Outputs 207, 128, 114, 194, 178,
print()
