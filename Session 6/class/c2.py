from tkinter import *
import random

# Tip -> tamame dastorat beyne TK va mainloop bayad bashe

# Step 1 -> sakhte bom naqashi
window = Tk()

# Step 3 -> amade sazi bome naqashi

# Step 4 -> tayin andaze safhe
window.geometry("500x500")

# Step 5 -> tayin titre safhe
window.title("My First App")

# Step 6 -> taqir range background
color = "#000000"
window.configure(bg=color)

# Label --> qarar dadane matn
# + text -> matn e morede nazaro neshon midad
# + font -> (font, size)
# + bg -> background color
# + fg -> foreground color
lbl1 = Label(window, text="Player 1", font=("bold", 30), bg=color, fg="red")
lbl1.place(x=50, y=50)

lbl2 = Label(window, text="Result !!", font=("bold", 20))
lbl2.place(x=150, y=200)


# + width -> arze kadre vorodi
# + bd -> atraf va to raftegi zaheri
en1 = Entry(window, font=("bold", 20), width=10, bd=5)
en1.place(x=200, y=50)

def dokme1():
    human_choice = en1.get()
    entekhabha = ["rock", "paper", "scissors"]
    entekhab_ai = random.choice(entekhabha)
    # Nested conditions
    if human_choice == entekhab_ai:
        lbl2.configure(text="Equal !")

    elif human_choice == "rock":
        if entekhab_ai == "scissors":
            lbl2.configure(text=f"Human = {human_choice} | AI = {entekhab_ai} | Winner is Human")
        else:
            lbl2.configure(text=f"Human = {human_choice} | AI = {entekhab_ai} | Winner is AI")


    elif human_choice == "paper":
        if entekhab_ai == "rock":
            lbl2.configure(text=f"Human = {human_choice} | AI = {entekhab_ai} | Winner is Human")

        else:
            lbl2.configure(text=f"Human = {human_choice} | AI = {entekhab_ai} | Winner is AI")


    elif human_choice == "scissors":
        if entekhab_ai == "paper":
            lbl2.configure(text=f"Human = {human_choice} | AI = {entekhab_ai} | Winner is Human")

        else:
            lbl2.configure(text=f"Human = {human_choice} | AI = {entekhab_ai} | Winner is AI")

    print("-------------------")


btn1 = Button(window, text="Click !", font=("bold", 20), width=15,
              bd=5, command=dokme1)
btn1.place(x=150, y= 150)


# Step 2 -> gozashtan paye baraye boom e naqashi
window.mainloop()