# Searching for items using the break keyword
shopping_list = ["milk", "pasta", "eggs", "bread", "cucumber"]

# # Defining the word to find and a variable for when it is found
# item_to_find = "bread"
# found_at = None

# Searching for an item that does not exist in the list
new_item_to_find = "bird"
new_found_at = None

# Searching for bread in the shopping list using index positions
# for index in range(len(shopping_list)):
#     if shopping_list[index] == new_item_to_find:
#         new_found_at = index
#         break

# Better way to write the code above
if new_item_to_find in shopping_list:
    new_found_at = shopping_list.index(new_item_to_find)

# Ensure the program prints something useful regardless of item found or not
if new_found_at is not None:
    print("Item found at position {}".format(new_found_at))
else:
    print("{} not found".format(new_item_to_find))
