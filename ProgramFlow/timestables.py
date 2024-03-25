# Working with nested loops
# Series of dashes added to separate the outputs of the outer loop
for i in range (1, 13):
    for j in range (1, 13):
        print("{0} times {1} is {2}".format(j, i, i * j))
    print("---------------")
