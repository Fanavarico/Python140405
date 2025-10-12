from tkinter import *

def btn_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

entry = Entry(root, width=20, font=("Arial", 20), borderwidth=3, relief="ridge", justify="right")
entry.place(x=20, y=20)

# Buttons layout (numbers and operators)
buttons = [
    ("7", 20, 80), ("8", 90, 80), ("9", 160, 80), ("/", 230, 80),
    ("4", 20, 140), ("5", 90, 140), ("6", 160, 140), ("*", 230, 140),
    ("1", 20, 200), ("2", 90, 200), ("3", 160, 200), ("-", 230, 200),
    ("0", 20, 260), (".", 90, 260), ("=", 160, 260), ("+", 230, 260),
]

for (text, x, y) in buttons:
    if text == "=":
        Button(root, text=text, width=5, height=2, font=("Arial", 12, "bold"), bg="#0078d7", fg="white",
               command=calculate).place(x=x, y=y)
    else:
        Button(root, text=text, width=5, height=2, font=("Arial", 12),
               command=lambda t=text: btn_click(t)).place(x=x, y=y)

Button(root, text="C", width=22, height=2, font=("Arial", 12), bg="#ff4747", fg="white",
       command=clear).place(x=20, y=320)

root.mainloop()