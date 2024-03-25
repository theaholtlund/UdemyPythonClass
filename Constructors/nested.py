# Working with nested list comprehensions
burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

# This is a flat list containing tuples
for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)

print()

# This is a nested list containing a list of tuples
# As such, it is made of four lists,m each containing the tuple
# This list iterates over the burgers for each topping
for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)

print()

# This list iterates over the toppings for each burger
for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
    print(nested_meals)
