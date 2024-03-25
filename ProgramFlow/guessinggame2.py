# Redefining the guessing game using while loops and random module
# Importing random module and setting range of random number
import random

# Defining some basic game logic
lowest_value = 1
highest_value = 10
answer = random.randint(lowest_value, highest_value)
print(answer)   # TODO: Remove after testing

# Initialise guess to any number that does not equal the answer
guess = 0
print("Please guess a number between {} and {}: ".format(lowest_value, highest_value))

# Evaluating the input using a while loop and break
# The player can end the game by pressing 0
while guess != answer:
    guess = int(input())
    if guess < answer:
        print("Please guess a higher number.")
    if guess > answer:
        print("Please guess a lower number.")
    if guess == answer:
        print("Well done, you guessed it!")
        break
    if guess == 0:
        print("Goodbye, thank you for playing!")
        break
