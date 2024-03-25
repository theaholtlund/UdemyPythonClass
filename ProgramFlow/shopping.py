# Working with lists, loops and the continue keyword
shopping_list = ["milk", "pasta", "eggs", "bread", "cucumber"]

# Skipping bread in the list using !=
# for item in shopping_list:
#     if item != "bread":
#         print("Buy " + item)

# Skipping bread in the list using continue
for item in shopping_list:
    if item == "bread":
        continue
    print("Buy " + item)
