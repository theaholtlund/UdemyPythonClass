# Importing the patients from the appropriate file
from data_remove_method import patients

# Defining what patients we want to do the trial for
trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

# Popping one patient at a time to examine their records
# Printing the patient along with what medication they are prescribed
# This way, the program ensures the patient is processed, and won't be processed again
while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)
