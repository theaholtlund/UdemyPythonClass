# Defining a dictionary with the travel options available in the program
travel_mode = {"1": "car", "2": "plane"}

# Creating a set with all items that will be needed for the camping trip
items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

# Restricted items that cannot be taken on a plane, if that is the mode of travel
restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

# Asking the user for their input on how they are traveling
print("Please choose your mode of travel:")
for key, value in travel_mode.items():
    print(f"{key}: {value}")
    # Python 3.5 and earlier
    # print("{}: {}".format(key, value))

# Initialising the input ot an invalid response, continue to prompt until a valid answer is given
mode = "-"
while mode not in travel_mode:
    mode = input("> ")

# Remove restricted items if the user is traveling by plane
# Discard is used instead of remove, since we do not care if the item is already in the list or not
# We just want it removed if it is there
if mode == "2":
    for restricted_item in restricted_items:
        items.discard(restricted_item)

# Print the packing list
print("You need to pack:")
for item in sorted(items):
    print(item)
