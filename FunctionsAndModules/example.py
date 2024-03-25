# Import required module
import random

# Anything in this output that starts with an underscore should not be changed
# Outputs with two underscores should not be changed at all
# This is useful information as there are no private variables in Python, everything is available
print(dir())

# Taking a closer look at the built-in modules
# Will return all the build-in modules of Python
print(dir(__builtins__))

# More user-friendly way to read the modules
for m in dir(__builtins__):
    print(m)

# The help function can be useful to get more information on a module
help(random.randint)
