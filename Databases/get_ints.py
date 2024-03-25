# Importing required modules
import sys


# Defining a function to allow users to add numbers
def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError: # EOF stands for End of File, signals that there are no inputs left
            sys.exit(1)
        except: # Should really be except ValueError:
            print("Invalid number entered, please try again")
        finally:
            print("The finally clause always executes")


# Calling the function to ask for user input
first_number = getint("Please enter first number ")
second_number = getint("Please enter second number ")

# Handling any errors that could arise from using the function
try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully")
