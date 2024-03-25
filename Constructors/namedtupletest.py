# Importing the data to work with
from data import basic_plants_list, plants_list

# Accessing the list using the named tuple
print(plants_list[0])

# Iterating over the list using the names tuple
for plant in plants_list:
    print(plant.name, plant[1])

print()

# Changing the lifecycle field in the list and confirming the output
example = plants_list[0]
print(example)
example = example._replace(lifecycle='Annual')
print(example)
