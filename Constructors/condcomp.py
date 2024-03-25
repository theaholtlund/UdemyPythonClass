# Define a list iof lists so work with
menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# Alternative solution without conditional expressions, using a for loop
# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#     else:
#         meals.append("a meal was skipped")
# print(meals)
#
# Solution with a conditional comprehension
# Syntax for conditional comprehension is new_list = [expression if condition else alternative for item in iterable]
# meals = [meal if "spam" not in meal else "a meal skipped" for meal in menu]
# print(meals)
#
# x = 15
# expression = "Twelve" if x == 12 else "unknown"
# print(expression)

# Using a conditional expression to solve the problem
# The syntax of a conditional expression is value_if_true if condition else value_if_false
for meal in menu:
    print(meal, "contains sausage" if "sausage" in meal else "contains bacon" if "bacon" in meal else "contains egg")

print()

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)
print()
menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)

# More work with conditional comprehensions and expressions
# meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)

fussy_meals = [meal for meal in menu if "spam" in meal or "eggs" in meal if not
               ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

fussy_meals = [meal for meal in menu if
               ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break

# Creating a new version of the fizzbuzz program using a conditional expression
# The order is important here, otherwise the expression will be true even if it should be something else
for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)
