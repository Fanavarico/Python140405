# menu
# add student
# delete student
# update student
# show students
from typing import final


# Start Function
def amir_menu():
    print("1| Add Student")
    print("2| Update Student")
    print("3| Delete Student")
    print("4| Show Students")
    print("0| Exit")

def save_to_file(data):
    with open("students_data.txt", "a") as file:
        file.write(f"{data} \n")

def read_file_data():
    with open("students_data.txt", "r") as file:
        for i in file.readlines():
            print(i)

def update_file_data(index_, new_data):
    with open("students_data.txt", "r+") as file:
        total_data = file.readlines()
        # ba try except khatahayi ke rokh mide ro modiriat mikonim
        try:
            total_data[index_] = f"{new_data} \n"
            file.seek(0) # tekon dadan pointer file be avale file
            file.truncate(0) # pak kardan ba etelawt qadimi az index 0 ta akhar file
            file.writelines(total_data) # neveshtan data jadid dakhele file

        except IndexError:
            print("Data not found !")

def delete_file_data(index_):
    with open("students_data.txt", "r+") as file:
        total_data = file.readlines()
        # ba try except khatahayi ke rokh mide ro modiriat mikonim
        try:
            total_data.pop(index_)
            file.seek(0)  # tekon dadan pointer file be avale file
            file.truncate(0)  # pak kardan ba etelawt qadimi az index 0 ta akhar file
            file.writelines(total_data)  # neveshtan data jadid dakhele file
        except IndexError:
            print("Data not found !")
# End Function

# Start Main
amir_menu()
choice = int(input("Enter Your Choice : "))
total = []

while choice != 0:

    if choice == 1:
        student_data = input("Name Last_name Age Score : ")
        save_to_file(student_data)

    elif choice == 2:
        read_file_data()
        index_user = int(input("Enter an index : "))
        student_data = input("Name Last_name Age Score : ")
        update_file_data(index_user, student_data)

    elif choice == 3:
        read_file_data()
        index_user = int(input("Enter an index : "))
        delete_file_data(index_user)

    elif choice == 4:
        read_file_data()

    else:
        print("Invalid Choice !")

    amir_menu()
    choice = int(input("Enter Your Choice : "))

# End Main