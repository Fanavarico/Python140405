from tkinter import *



win3 = Tk()
win3.title("Sum App")
win3.geometry("250x120")

entry1 = Entry(win3)
entry1.place(x=50, y=20)
entry2 = Entry(win3)
entry2.place(x=50, y=50)

def calc_sum():
    a = int(entry1.get())
    b = int(entry2.get())
    print("Sum =", a + b)

btn2 = Button(win3, text="Calculate", command=calc_sum)
btn2.place(x=90, y=80)

win3.mainloop()
