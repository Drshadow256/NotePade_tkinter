from tkinter import *

w = Tk()
w.title('NOTEPAD')

def load():
    w2 = Tk()
    w2.resizable(0, 0)
    def open_file():
        with open(f"{e.get()}.txt") as f:
            data = f.read()
        t.insert(INSERT,data)

    Label(w2,text='name`s file of txt : ',font='calibri 20').pack()
    e = Entry(w2)
    e.pack()
    Button(w2,text='open',command=open_file).pack()
    w2.mainloop()

def take():
    with open('file.txt','w') as f:
        f.write(t.get(1.0,END))

t = Text(w)
t.pack()

Button(w,text='save file',command=take).pack()
Button(w,text='load file ',command=load).pack()
Label(w,text='(drshadoo86@gmail.com)برنامه نویس:مسعود شایق').pack(side='bottom')

w.mainloop()









