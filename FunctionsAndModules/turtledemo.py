# Importing the turtle module, which is a simple way to create turtle graphics
from turtle import *

# If we define this after the import, this is what the done() function will try to execute
# done = "Well done, you have finished your drawing"

# Define workflow for turtle graphics
forward(150)
right(250)
forward(150)
circle(75)

done()
print(done)
