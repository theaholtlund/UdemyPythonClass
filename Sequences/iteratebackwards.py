# Create list and define values to iterate over
data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# Remove values that are too low or too high
# Range to generate sequence of indices starting from last list index
# The last index of the list would be (len(data) - 1)
# -1: The loop moves backward by one index with each iteration
# Other -1: Until it reaches index 0, which would have index position -1
# for index in range(len(data) - 1, - 1, - 1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]
#
# print(data)

# There is also an easier way to do this, using the reversed function
# Define top_index to get the correct index values for the list
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
print(data)
