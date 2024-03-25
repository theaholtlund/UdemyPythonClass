# Defining some sets to test for subsets and supersets
animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }

birds = {'Robin', 'Swallow', 'Wren'}

# Checking whether the sets are supersets and subsets of the other set
# The first two statements should equate to True, while the last one should equate to False
print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'animals is a superset of birds: {animals.issuperset(birds)}')
print(f'birds is a superset of animals: {birds.issuperset(animals)}')

# The first statement checks if birds is a subset of animals, while the second checks if it is a proper subset
print(birds <= animals)
print(birds < animals)

# Separating the outputs for better readability
print('*' * 80)

# Duplicate the birds set with a new name for the set
# Then seeing if the set is equal, a subset and a proper subset of the birds set
garden_birds = {'Swallow', 'Wren', 'Robin'}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds)

# Separating the outputs for better readability
print('*' * 80)
