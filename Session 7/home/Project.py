# menu
# add student
# delete student
# update student
# show students


# Start Function
def amir_menu():
    print("1| Add Student")
    print("2| Update Student")
    print("3| Delete Student")
    print("4| Show Students")
    print("0| Exit")

def elina_read_data(data):
    for std in data:
        print(std)

# End Function

# Start Main
amir_menu()
choice = int(input("Enter Your Choice : "))
total = []

while choice != 0:

    if choice == 1:
        student_data = input("Name Last_name Age Score : ").split()
        total.append(student_data)

    elif choice == 2:
        elina_read_data(total)
        index_user = int(input("Enter an index : "))
        student_data = input("Name Last_name Age Score : ").split()
        total[index_user] = student_data

    elif choice == 3:
        elina_read_data(total)
        index_user = int(input("Enter an index : "))
        print("deleted data = ", total.pop(index_user))

    elif choice == 4:
        elina_read_data(total)

    else:
        print("Invalid Choice !")

    amir_menu()
    choice = int(input("Enter Your Choice : "))

# End Main