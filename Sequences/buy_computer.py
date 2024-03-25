# Define some lists to work on
available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
current_choice = "-"
computer_parts = []

# Working with the append method
# while current_choice != "0":
#     if current_choice in "12345":
#         print("Adding {}".format(current_choice))
#         if current_choice == '1':
#             computer_parts.append("computer")
#         elif current_choice == '2':
#             computer_parts.append("monitor")
#         elif current_choice == '3':
#             computer_parts.append("keyboard")
#         elif current_choice == '4':
#             computer_parts.append("mouse")
#         elif current_choice == '5':
#             computer_parts.append("mouse mat")
#
#     else:
#         print("Please add options from the list below:")
#         print("1: computer")
#         print("2: monitor")
#         print("3: keyboard")
#         print("4: mouse")
#         print("5: mouse mat")
#         print("0: to finish")
#
#     current_choice = input()
#
# print(computer_parts)

# Improving the code written above, using the enumerate function
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != "0":
    if current_choice in valid_choices:

        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # It will already be chosen, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)
