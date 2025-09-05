from tkinter import *

w = Tk()
w.geometry('500x500')

def add():
    lb.insert(END,elb.get())

def clear():
    lb.delete(0,END)

elb = Entry(w)
elb.pack()

Button(w,text='add',command=add).pack()
Button(w,text='clear',command=clear).pack()
lb = Listbox(w)
lb.pack()



w.mainloop()
