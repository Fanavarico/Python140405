# Start Function

def amir_menu():
    print("1| Jam")
    print("2| Tafriq")
    print("3| Taqsim")
    print("4| Zarb")
    print("0| Exit")

def elina_choice():
    return int(input("Enter Your choice : "))

def arshia_entekhab():
    n1 = int(input("Enter number 1 : "))
    n2 = int(input("Enter number 2 : "))
    return n1, n2

# End Function

# Start Main

amir_menu()
choice = elina_choice()

while choice != 0:

    if choice == 1:
        entekhab1, entekhab2 = arshia_entekhab()
        print(f"Jam = {entekhab1 + entekhab2}")

    elif choice == 2:
        entekhab1, entekhab2 = arshia_entekhab()
        print(f"Tafriq = {entekhab1 - entekhab2}")

    elif choice == 3:
        entekhab1, entekhab2 = arshia_entekhab()
        print(f"Taqsim = {entekhab1 / entekhab2}")

    elif choice == 4:
        entekhab1, entekhab2 = arshia_entekhab()
        print(f"Zarb = {entekhab1 * entekhab2}")

    else:
        print("Invalid choice !")


    amir_menu()
    choice = elina_choice()

# End Main