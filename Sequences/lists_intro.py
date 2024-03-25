# Creating a basic list with list elements
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"]

# Loop to print out elements
for part in computer_parts:
    print(part)

# It is also possible to print elements in a list by index position
print(computer_parts[2])

# Lists can also be sliced in the same way strings are sliced
# Slicing a list will produce a new list with the elements accessed
print(computer_parts[-1])
print(computer_parts[0:3])
