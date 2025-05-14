import tkinter as tk
from tkinter import *

form= tk.Tk()
Label(form, text="First Name").grid(row=0)
Label(form, text="Last Name").grid(row=1)
Label(form, text="Email").grid(row=2)
Label(form, text="Password").grid(row=3)

var1= IntVar()
Checkbutton(form, text="Applied", variable=var1).grid(row=4, sticky=W, column=0)
var2= IntVar()
Checkbutton(form, text="Not Applied", variable=var2).grid(row=4,sticky=W, column=1)

Lb= Listbox(form)
Lb.insert(1,"Python")
Lb.insert(2,"Java")
Lb.insert(3,"C++")
Lb.insert(4,"JavaScript")
Lb.grid(row=5, column=1)


r1=Entry(form)
r2=Entry(form)
r3=Entry(form)
r4=Entry(form)


r1.grid(row=0, column=1)
r2.grid(row=1, column=1)
r3.grid(row=2, column=1)
r4.grid(row=3, column=1)

def submit():
    print("First Name: ", r1.get())
    print("Last Name: ", r2.get())
    print("Email: ", r3.get())
    print("Password: ", r4.get())

Button(form, text="Submit", command=submit).grid(row=6, column=1)
Button(form, text="Clear", command=lambda:print("Not Submitted")).grid(row=6, column=0)
form.title("Form")
form.geometry("300x200")





form.mainloop()