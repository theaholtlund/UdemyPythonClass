# Loop block example
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {}".format(i, i ** 2, i ** 3))
    print("*" * 80)

# More testing with blocks.
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# # Checking if the person is old enough to vote, using an if statement
# if age >= 18:
#     print("You're old enough to vote!")
#     print("Please put an X in the box.")
# elif age == 900:
#     print("Sorry, Yoda, you die in Return of the Jedi.")
# else:
#     print("Please come back in {0} years".format(18 - age))

# Rewriting the program using an elif statement
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi.")
else:
    print("You're old enough to vote!")
    print("Please put an X in the box.")
