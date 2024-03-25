# Define dictionary to store values
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

# Accessing elements in the dictionary
my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

# The dot get method can also be used to access values in a dictionary
# The method will not crash the program, rather return None if the value is not found
# This method can be useful if you are unsure of whether the key existsa or not
learner = vehicles.get('er5')
print(learner)

# Adding new value to a dictionary is done by assigning its key as shown below
vehicles["starfighter"] = "Lockheed F-104"

# Updating the value of a dictionary element can be done by simply assigning a new value to the key
vehicles['virago'] = "Yamaha XV535"

# Values can be deleted from a dictionary by using the del keyword
del vehicles["starfighter"]

# Values can also be deleted using the pop method, which will crash if the key is not found
# You can prevent it from crashing if the key is not found by providing a default value
# Pop will return the value, or the default value if it was not found
car = vehicles.pop("f1", "Not present")
print(car)

# Dictionaries are also iterable, where you can iterate over the keys
# for key in vehicles:
#     print(key, vehicles[key], sep=", ")
for key, value in vehicles.items():
    print(key, value, sep=", ")
