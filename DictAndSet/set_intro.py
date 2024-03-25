# Defining a set to work with, with curly braces that are used for sets
# Had we used square brackets, we would have had a list
# Has we used parenthesis, or no brackets at all, we would have had a tuple
farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}

# Print the set to see that the order of which the items appear in are different every time
# This highlights the points of sets being a collection of unordered items
print(farm_animals)

# Fixing a bug in an earlier challenge from the course, now using sets
# Using the set function to create a new set with every item in the iterable
# Set is faster than list here, because they use hash codes, while lists use linear search
# When checking for membership in a set, Python uses the hash code to find out where the item should be
# As such, going directly to the item in the hash table is faster than checking through every item
# Using a set literal also optimises the program, as Python does not have to make the set every time we run the code
choice = "-"  # Initialise choice to something invalid
while choice != "0":
    # if choice in set("12345"):
    if choice in {"1", "2", "3", "4", "5"}:
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()
