# Defining a class to work with OOP
# We can think of a class as a template from which objects can be created
class Kettle(object):

    # Defining a class attribute that all objects will share
    # Here, all instances will share a single version of this class attribute
    power_source = "electricity"

    # Initialising the function, or method
    # This becomes a method of the Kettle class
    # When we create objects of the Kettle class, they will have a make and a price
    # Make and price are also attributes of the objects later defined for the type Kettle
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    # Defining another method for the Kettle class
    def switch_on(self):
        self.on = True


# Kenwood is an instance of the Kettle class
# We can also say that Kenwood is an object of the type Kettle
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

# Changing the price to make sure it is changed
# Retrieves the price from the Kenwood instance of the Kettle class
kenwood.price = 12.75
print(kenwood.price)

# Creating a new instance of the Kettle class
hamilton = Kettle("Hamilton", 14.55)

# Printing out the attributes of the objects
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

# Because Kenwood and Hamilton are objects, we can specify their attributes in the replacement fields
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: Template for creating objects, and all objects created using the same class will have the same characteristics
Object: An instance of a class
Instantiate: Create an instance of a class
Method: A function defined in a class
Attribute: A variable bound to an instance of a class
"""

# Using the switch method for the Hamilton object
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# Seeing that we do not need to specify self when calling the method of the class
# The value of self is then indirectly specified, by adding Kenwood
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

# Just like everything else in Python, classes are dynamic and can be modified after creation
# The Kenwood instance of the Kettle class not has another data attribute called power
# Variables come into existence the first time they are assigned a value
# The same goes for instance variables, and instance variables are the same as data attributes
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power) # Hamilton will not have a power attribute just because Kenwood does

# Showing that all instances, including the class itself, will share the value of the class attribute
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

# We can also access the namespace via the dict attribute
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
