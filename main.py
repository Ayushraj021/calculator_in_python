import tkinter as tk
from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Calculator")

# Entry field to display the result
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button click function
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# Define button clear function
def button_clear():
    entry.delete(0, END)

# Define button equal function
def button_equal():
    try:
        result = eval(entry.get())  # Calculate the expression
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Define button for operations
def button_operation(op):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + op)

# Create number buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Create operation buttons
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_operation("+"))
button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: button_operation("-"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_operation("*"))
button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: button_operation("/"))

button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=78, pady=20, command=button_clear)

# Place buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Start the GUI loop
root.mainloop()