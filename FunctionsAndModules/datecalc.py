# Import required modules
import time
import random

# Using the perf_counter() function for the game instead
# Provides a way to measure elapsed time with high precision, and is commonly used for benchmarking
# We could also use the monotonic() function, used to obtain a clock that continually increases at a constant rate
# It is unaffected by system clock adjustments
# We could also use the process_time() function, used to measure the CPU time or the amount of time spent
# It is measured by the current process in executing its code
# from time import time as my_timer
# from time import perf_counter as my_timer
# from time import monotonic as my_timer
from time import process_time as my_timer

# Time.gmtime() takes a time in seconds since the epoch (January 1, 1970)
# Returns a struct_time object representing the corresponding UTC time
# In this case, time.gmtime(0) is called with 0 as the argument, which represents the epoch time
print(time.gmtime(0))

# Time.localtime() returns an object representing the current local time
print(time.localtime())

# time.time() returns the current time in seconds since the epoch as a floating-point number
print(time.time())

# Working with the time module
# The tm is a prefix used to access the attributes of the struct_time object
# The year, month and day are listed in two different ways, which gives identical outputs
time_here = time.localtime()
print(time_here)
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)

# Creating a simple guessing game with time
input("Press enter to start")

# Specifying a random delay between 1 and 6 seconds
# Recording the start time before enter was pressed
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

# Then recording the end time after enter was pressed
end_time = my_timer()

# Calculating the difference between the start time and end time
# Strftime stands for string from time, which can be used to format the tiem tuple to a more usable format
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
print("Your reaction time was {} seconds".format(end_time - start_time))
