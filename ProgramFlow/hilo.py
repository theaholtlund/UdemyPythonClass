# Using the binary chop algorithm to create a guessing game
low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

# Variable to store the number of guesses
# With binary search, or binary chop, this should be less than 10
guesses = 1

# Creating the guessing game logic
# Calculate midpoint between low and high value to produce the next guess
# When low == high, we know we have got the right number
while low != high:
    print("\tGuessing the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter H or L, or C if my guess was correct. "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. Low end of the range becomes one greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. High end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        # This will cause the else block below not to be executed
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter H, L or C for this program")

    # guesses = guesses + 1
    # Using augmented assignment to improve the code, making it more efficient
    guesses += 1

# Using the else statement in the loop to indicate what should happen when the loop is broken
# The loop will be broken when low == high, as indicated in the while loop
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))
