# Calculator Project
# tip -> payan na moshakhas

# Step 1 --> namayesh menu
# Adad
# Step 2 --> bar asase entekhab yek kari anjam bedim

# Step 1 -> Done
# Menu -> namayesh matne
print("----------Menu----------")
print("1 | Jam")
print("2 | Tafriq")
print("3 | Zarb")
print("4 | Taqsim")
print("0 | Exit")
choice = int(input("Enter Your Choice : "))
print("----------Menu----------")


while choice != 0:

    if choice == 1:
        n1 = int(input("Enter Your Number 1 : "))
        n2 = int(input("Enter Your Number 2 : "))
        print(f"Hasel Jam = {n1 + n2}")

    elif choice == 2:
        n1 = int(input("Enter Your Number 1 : "))
        n2 = int(input("Enter Your Number 2 : "))
        print(f"Hasel Tafriq = {n1 - n2}")

    elif choice == 3:
        n1 = int(input("Enter Your Number 1 : "))
        n2 = int(input("Enter Your Number 2 : "))
        print(f"Hasel Zarb = {n1 * n2}")

    elif choice == 4:
        n1 = int(input("Enter Your Number 1 : "))
        n2 = int(input("Enter Your Number 2 : "))
        print(f"Hasel Taqsim = {n1 / n2}")

    else:
        print("Invalid Choice !!")

    print("----------Menu----------")
    print("1 | Jam")
    print("2 | Tafriq")
    print("3 | Zarb")
    print("4 | Taqsim")
    print("0 | Exit")
    choice = int(input("Enter Your Choice : "))
    print("----------Menu----------")

print("Thanks for using my firs APP \u2764\uFE0F")