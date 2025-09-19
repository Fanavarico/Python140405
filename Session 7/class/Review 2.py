from tkinter import *
# GUI --> Graphical User Interface
# UI -> User Interface
# UX -> User Experience

# Library
# tkinter -> built-in
# moderntkiner - cosumetkinter
# PyQt5
# Kivy -> android - ios

# Tip -> hameye code ha bayne step 1 va 2

# Step 1 -> sakhte bom
bom = Tk()
# Tanzimat avalie - configure
# Step 3 --> Title
bom.title("app 1")
# step 4 --> andaze
bom.geometry("300x300")
# step 5 --> resize
bom.resizable(width=False, height=False)

# Widgets -> Label - Button - Entry
# Label -> matn ro safhe
lbl1 = Label(bom, text="Hello", font=("bold", 20))
lbl1.place(x=20, y=50)

# Entry -> daryaft vorodi az karbar
en1 = Entry(bom, width=15, bd=5, font=("bold", 20))
en1.place(x=70, y=50)

# Button -> dokme roye safhe
btn1 = Button(bom, text="Click", width=5, font=("bold", 20))
btn1.place(x=40, y=150)

# Step 2 --> paye bom ro qarar midim
bom.mainloop()