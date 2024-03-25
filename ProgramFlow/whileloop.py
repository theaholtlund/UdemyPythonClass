# Creating a basic while loop
# The condition of while loops must be initialised before start
# We also need somewhere in the loop for the condition to become False
i = 0
while i < 5:
    print("i is now {}".format(i))
    i += 1

# Maneuvering an adventure game using a while loop
available_exits = ["north", "south", "east", "west"]
# Initialise chosen exit and loop with something that is not any of the available exits
chosen_exit = ""

# Casefold is used to account for Python case sensitivity for inputs
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

# Else statement for the loop if it is continued
# This code will be executed if the player does not quit the game
else:
    print("Aren't you glad you got out of there")
