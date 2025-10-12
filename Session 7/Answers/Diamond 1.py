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

def qoli_save_to_file(operation, counter,  num1, num2):
    calculate = eval(f"{num1}{operation}{num2}")
    result = f"{counter} | {num1} {operation} {num2} = {calculate}"
    print(result)
    with open("calculator_result.txt", "a") as file:
        file.write(result + "\n")


# End Function

# Start Main
counter = 1
amir_menu()
choice = elina_choice()

while choice != 0:

    if choice == 1:
        entekhab1, entekhab2 = arshia_entekhab()
        qoli_save_to_file("+", counter, entekhab1, entekhab2)
        counter += 1

    elif choice == 2:
        entekhab1, entekhab2 = arshia_entekhab()
        qoli_save_to_file("-", counter, entekhab1, entekhab2)
        counter += 1

    elif choice == 3:
        entekhab1, entekhab2 = arshia_entekhab()
        qoli_save_to_file("/", counter, entekhab1, entekhab2)
        counter += 1

    elif choice == 4:
        entekhab1, entekhab2 = arshia_entekhab()
        qoli_save_to_file("*", counter, entekhab1, entekhab2)
        counter += 1

    else:
        print("Invalid choice !")


    amir_menu()
    choice = elina_choice()

# End Main