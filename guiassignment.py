#GUI Program
from tkinter import *
root=Tk()
root.title("GUI Program")
root.geometry('500x500')
hellobtn=Button(root,text="Hello")
hellobtn.grid(row=1,column=1)
exitbtn=Button(root,text="Exit")
exitbtn.grid(row=1,column=2)
root.mainloop()
