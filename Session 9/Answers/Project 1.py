from tkinter import *

def save_contact():
    name = name_entry.get()
    family = family_entry.get()
    relation = relation_entry.get()
    phone = phone_entry.get()

    if not (name and family and relation and phone):
        status_label.config(text="⚠️ Please fill all fields!", fg="red")
        return

    with open("contacts.txt", "a") as f:
        f.write(f"{name}, {family}, {relation}, {phone}\n")

    status_label.config(text="✅ Contact saved successfully!", fg="green")

    name_entry.delete(0, END)
    family_entry.delete(0, END)
    relation_entry.delete(0, END)
    phone_entry.delete(0, END)

# ---- GUI setup ----
root = Tk()
root.title("Contact Manager")
root.geometry("400x300")
root.configure(bg="#eaf6ff")

# Labels and Entries
Label(root, text="Name:", bg="#eaf6ff", fg="black", font=("Arial", 12)).place(x=30, y=30)
Label(root, text="Family:", bg="#eaf6ff", fg="black",font=("Arial", 12)).place(x=30, y=70)
Label(root, text="Relation:", bg="#eaf6ff", fg="black",font=("Arial", 12)).place(x=30, y=110)
Label(root, text="Phone:", bg="#eaf6ff", fg="black",font=("Arial", 12)).place(x=30, y=150)

name_entry = Entry(root, width=25, font=("Arial", 12))
family_entry = Entry(root, width=25, font=("Arial", 12))
relation_entry = Entry(root, width=25, font=("Arial", 12))
phone_entry = Entry(root, width=25, font=("Arial", 12))

name_entry.place(x=130, y=30)
family_entry.place(x=130, y=70)
relation_entry.place(x=130, y=110)
phone_entry.place(x=130, y=150)

# Save Button
Button(root, text="Save Contact", font=("Arial", 12, "bold"),
       command=save_contact).place(x=130, y=200)

# Status Label
status_label = Label(root, text="", bg="#eaf6ff", font=("Arial", 10))
status_label.place(x=130, y=250)

root.mainloop()