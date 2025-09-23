from tkinter import *

win4 = Tk()
win4.title("Name App")
win4.geometry("300x120")

entry_name = Entry(win4)
entry_name.place(x=50, y=20)
entry_last = Entry(win4)
entry_last.place(x=50, y=50)

def show_name():
    full = entry_name.get() + " " + entry_last.get()
    print("Full Name:", full)


btn3 = Button(win4, text="Show Name", command=show_name)
btn3.place(x=100, y=80)

win4.mainloop()   