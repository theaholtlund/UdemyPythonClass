# Importing the module
# from blackjack import *
import blackjack

# An attribute of the __name__ module is set to be the name of the module
# This is the file name without path or extension
# Preventing a module from running upon import can be done by checking the value of the name attribute
# Then, indicating that it should only execute the code if it has a value
# This can be done by setting something like if __name__ == __main__ in the import script
print(__name__)

# After having defined a play() function in the imported file, we can now play the game by calling it
# blackjack.play()

# Check that the cards list is printed, to confirm the cards list is imported correctly and not modified
print(blackjack.cards)

# Confirming that we get a warning when trying to use a protected variable, but also seeing that it is still possible
blackjack._deal_card(blackjack.dealer_card_frame)

# Seeing what we have as globals now
# Had we used the from blackjack import * statement, all the variables and functions would have shown too
# Basically, everything from the blackjack module namespace would appear in this module namespace
# However, variables indicated as protected by using a _ in front of the name would not be imported
g = sorted(globals())

for x in g:
    print(x)

# Defining and working with a throwaway variable
personal_details = ("Thea", 25, "Norway")
name, _, country = personal_details
print(name, country)
print(_)
