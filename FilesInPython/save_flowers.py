# Define data to export and save
data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# Specify name of file to be saved
plants_filename = "flowers_print.txt"

# Save the file, specifying the need to write with the "w" mode parameter
with open(plants_filename, "w") as plants:
    for plant in data:
        print(plant, file=plants) # Tell print to sent the text to the file

# Define a new list to display the results
new_list = []

# Read the data back after saving it to the file
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip()) # Add each string to the new_list list
#
# print(new_list)

# Different approach to read the data back after saving it to the file
plants_filename = "flowers_write.txt"

with open(plants_filename, "w") as plants:
    for plant in data:
        plants.write(plant) # Use the write method of the file name, which is plants
