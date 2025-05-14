import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("GUI")

label= tk.Label(window, text="Welcome to the Tkinter GUI !").pack()

button = tk.Button(window, text="Click Me", command=lambda: print("Button Clicked!"))
button.pack()

window.mainloop()