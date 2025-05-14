import tkinter as tk
from tkinter import *
from tkinter import messagebox

window=tk.Tk()

Label(window,text="first name").grid(row=0)
Label(window,text="last name").grid(row=1)
Label(window,text="email").grid(row=2)
Label(window,text="password").grid(row=3)

var1=IntVar()
Checkbutton(window,text="Applied",variable=var1).grid(row=4,sticky=W,column=0)
var2=IntVar()
Checkbutton(window,text="Not Applied",variable=var2).grid(row=4,sticky=W,column=1)


# sr= Scrollbar(window)
# sr.grid(row=5,column=2,sticky='ns')
# sr.pack(side=RIGHT,fill=Y)
# mylist=Listbox(window, yscrollcommand=sr.set)


# for i in range(200):
#     mylist.insert(END, "List item" + str(i))

# mylist.pack(side=LEFT, fill=BOTH)
# sr.config(command=mylist.yview)



neo1=Entry(window)
neo2=Entry(window)
neo3=Entry(window)
neo4=Entry(window)


neo1.grid(row=0,column=1)
neo2.grid(row=1,column=1)
neo3.grid(row=2,column=1)
neo4.grid(row=3,column=1)

def submit():
    print("first name:", neo1.get())
    print("last name:", neo2.get())
    print("email:", neo3.get())
    print("password:", neo4.get())
    print("Applied:", var1.get())
    print("Not Applied:", var2.get())

    messagebox.showinfo('title', "Successfully submitted")

Button(window,text="Submit", command=submit).grid(row=6, column=1)

Button(window,text="Clear", command=lambda: print("Empty form")).grid(row=6, column=0)





window.title("Form")
window.geometry("300x200")

window.mainloop()