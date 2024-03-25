# Defining two sets to work with when finding the union
farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

# The union can be found in several ways
# All these approaches will have the same output
# Finding the union based on farm_animals
all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)

# Finding the union based on wild_animals
all_animals_2 = wild_animals.union(farm_animals)
print(all_animals_2)

# Finding the union using the pipe character
all_animals_3 = wild_animals | farm_animals
print(all_animals_3)

# A more practical application can be constructed based on the patient and prescriptions case
from data_remove_method import adverse_interactions

# Finding the adverse interactions for the medication
# The next set created in the for loop is the union of whatever is built up so far
# The update() method to update the set instead of creating a new one every time around the loop
meds_to_watch = set()
for interaction in adverse_interactions:
    # meds_to_watch = meds_to_watch.union(interaction)
    # meds_to_watch.update(interaction)
    meds_to_watch |= interaction # Alternative to the code on the line above, does the same thing

# Another way this could be done is by unpacking the list, as it is a sequence
meds_to_watch.update(*adverse_interactions)
print(sorted(meds_to_watch))

# A smart, different way to print all the sorted medication, each on a new line
# This is done by unpacking the list of sorted medications to watch
print(*sorted(meds_to_watch), sep="\n")
