# CRUD -> Dictionary
# Car Management System

# company - model - price - color - kilometer - top speed - 0-100
# car1: []
# car2: []
# car3: []

# CRUD
# Create
# Read
# Update
# Delete

# Start Function
def menu():
    print("1| Add a Car")
    print("2| Update a Car")
    print("3| Delete a Car")
    print("4| Show all Cars")
    print("0| Exit")

def user_choice():
    return int(input("Enter Your Choice : "))

def show_all_cars(total):
    for key, value in cars.items():
        print(key, value)
# End Function

# Start Main

menu()
choice = user_choice()
cars = {}
counter = 1

while choice != 0:
    if choice == 1:
        data = input("company - model - price - color - kilometer - top speed - 0-100 : ").split()
        # way 1
        # adad_car = "car" + str(counter)
        # cars[adad_car] = data

        # way 2
        cars[f"car{counter}"] = data
        counter += 1


    elif choice == 2:
        show_all_cars(cars)
        key_ = input("Enter Related Key : ")
        new_data = input("company - model - price - color - kilometer - top speed - 0-100 : ").split()
        cars[key_] = new_data

    elif choice == 3:
        show_all_cars(cars)
        key_ = input("Enter Related Key : ")
        cars.pop(key_)


    elif choice == 4:
        show_all_cars(cars)

    else:
        print("Wrong choice !")

    print("--------------------")
    menu()
    choice = user_choice()
    print("--------------------")

# End Main

# benz c200 2000 black 100000 200 10
# volvo XC90 20000 white 0 250 15