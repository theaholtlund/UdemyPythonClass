# Import required modules
import os


# Define a function to list the directories
# As seen, recursive functions work well with recursive structures such as file systems
def list_directories(s):

    # Recursive function list visit found directories
    def dir_list(d):
        nonlocal tab_stop # Nonlocal used to declare a variable inside a nested function
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + " does not exist")


list_directories('.')
