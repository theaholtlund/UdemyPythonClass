# Import required modules
import webbrowser

# Opening a web browser with the webbrowser module
webbrowser.open("https://www.python.org/", new=0)

# Using the get() method to specify the browser
safari = webbrowser.get(using="safari")
safari.open("https://www.python.org/")

# Learning more about reading and understanding documentation
help(webbrowser)

# Using the print function to look more into documentation
for i in range(10):
    print(i, 1, sep=": ", end=",")
