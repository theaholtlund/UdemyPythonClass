# Import required modules
import timeit

# Defining a list of lists to work with
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


# Defining a function to check for spam using list comprehension
def spamless_comp():
    # meals = [meal for meal in menu if "spam" not in meal]
    meals = [meal for meal in menu if not_spam(meal)]
    return meals


print("-" * 40)


# Defining a function to find find the meals without spam
def not_spam(meal_list: list):
    return "spam" not in meal_list


# Using the filter() function to accomplish the same thing
def spamless_filter():
    spamless_meals = list(filter(not_spam, menu))
    return spamless_meals


# Using the timeit module to check the performance of each function
if __name__ == '__main__':
    print(spamless_comp())
    print(spamless_filter())
    print(timeit.timeit(spamless_comp, number=100000))
    print(timeit.timeit(spamless_filter, number=100000))
