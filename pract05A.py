# Practical 06

# This program won't run in Online Compiler
from tkinter import *
import tkinter.font as font
from tkinter.ttk import Combobox
window=Tk()

#create Font object
myFont = font.Font(family='Courier')

btn=Button(window, text="This is Button widget",width=25,height=3, bg='blue', fg="yellow",font=myFont)
btn.place(x=80, y=100)

lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)

txtfld=Entry(window, text="This is Entry Widget", bd=5 ,bg="yellow", fg="Black")
txtfld.place(x=80, y=180)

v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="male", variable=v0,value=1)
r2=Radiobutton(window, text="female", variable=v0,value=2)
r1.place(x=100,y=20)
r2.place(x=180, y=20)

v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Cricket", variable = v1)
C2 = Checkbutton(window, text = "Tennis", variable = v2)
C1.place(x=100, y=220)
C2.place(x=180, y=220)

data=("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=60, y=250)


lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=250, y=250)

window.title('Hello Python')
window.geometry("400x450+10+10")
window.mainloop()