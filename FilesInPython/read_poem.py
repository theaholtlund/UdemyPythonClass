# Define a variable for the file
jabber = open("Jabberwocky.txt", "r")

# Do something with the contents of the text file
# Also printing the length of each line to confirm the count of characters
# Various approaches to avoid double space, both from print and one from newlines in the text file
for line in jabber:
    print(line.strip())
    # print(line, end="")
    # print(len(line))

jabber.close

# This process can be performed in a better way
# When using the with statement, and not a function, we don't get a file object returned
# No need to specify that we then want to close the file, will happen automatically
# Linux and Mac OS will often have UTF-8 as the default encoding, but it might have to be specified for Windows
with open("Jabberwocky.txt", "r", encoding="utf-8") as jabber:
    for line in jabber:
        print(line.rstrip())

# Storing the lines in memory, as done below, allows us to execute some additional processing
# With this approach, every line is read into a list in Python, so they are only useful for smaller files
with open("Jabberwocky.txt", "r") as jabber:
    lines = jabber.readlines()

print(lines)
for line in reversed(lines):
    print(line, end="") # Do some processing in reverse order
