# Import the data from the appropriate file
from data_remove_method import *

# Select some patients from the trial
trial_patients = ["Denise", "Eddie", "Frank", "Georgia"]

# Remove Warfarin and replace it with Edoxaban instead
# With remove, we get an error if we are trying to remove something that is not already there
# This way, we know no patients will be prescribed Edoxaban if they were not taking Warfarin
# We can also improve the program by checking the set before attempting to add or remove prescriptions
# for patient in trial_patients:
#     prescription = patients[patient]
#     if warfarin in prescription:
#         prescription.remove(warfarin)
#         prescription.add(edoxaban)
#     else:
#         print(f"Patient {patient} is not taking Warfarin")
#         print(f"Please remove {patient} from the trial")
#     print(patient, prescription)

# An even better solution would be to raise an exception error
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin"         
              f"Please remove {patient} from the trial")
    print(patient, prescription)
