# Defining game logic and an answer
answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

# # Using if, elif and else to evaluate the input
# if guess < answer:
#     print("Please guess a higher number.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > answer:
#     print("Please guess a lower number.")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("That is the correct number!")

# Using conditional operators to evaluate the input
if guess != answer:
    if guess < answer:
        print("Please guess a higher number.")
    else:
        print("Please guess a lower number.")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly.")
else:
    print("Nice! You got it the first time!")
