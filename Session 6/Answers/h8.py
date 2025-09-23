from tkinter import *

win2 = Tk()
win2.title("Hello User")
win2.geometry("250x100")

entry = Entry(win2)
entry.place(x=50, y=20)

def say_hello():
    name = entry.get()
    print("Hello", name)

btn = Button(win2, text="Say Hello", command=say_hello)
btn.place(x=80, y=50)

win2.mainloop()