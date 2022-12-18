#GUI prpgram to convert celsius to fahrenheit
from tkinter import *
from tkinter import messagebox
global c
def conversion():
    c=float(ent1.get())
    f=c*(9/5)+32
    lb2.config(text="Given Temperature "+str(c)+" in Fahrenheit scale is: "+str(f))
#MAIN PROGRAM
root=Tk()
root.title("TEMPERATURE CONVERSION")
lbl=Label(root,text="Enter Temperature in Celsius Scale:")
lbl.grid(row=1,column=1)
#ENTRYBOX
ent1=Entry(root,width=10)
ent1.grid(row=1,column=2)
convert=Button(root,text="Convert",command=conversion)
convert.grid(row=2,column=2)
lb2=Label(root,text="")
lb2.grid(row=3,column=2)
