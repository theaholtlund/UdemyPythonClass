# Importing Tkinter, which is the standard GUI toolkit included with Python
# It is based on the Tk GUI framework
try:
    import tkinter
except ImportError:  # Just for Python 2
    import Tkinter as tkinter

# tkinter._test()

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk() # Root window, everything else must be placed within or in child window

# Giving the window a title and a size
mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400') # Set window size, plus specify screen location

# Label the window
label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

# Setting up a grid on the left side of the window
leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

# Use pack geometry manager, canvas will be on left hand side of the window
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

# Add some buttons to the right side of the window
rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# Configure the columns of the grid
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

# Configure window appearance
leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

# Configure placement in the grid
rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')
mainWindow.mainloop()


# Pass control over to Tkinter by calling the mainloop() method
mainWindow.mainloop()
