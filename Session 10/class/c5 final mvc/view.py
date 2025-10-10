from controller import Manager
from models import Student
# Menu
def menu():
    print("1| Add Student")
    print("2| Update Student")
    print("3| Delete Student")
    print("4| Show all Students")
    print("0| Exit")
    return int(input("Enter Choice : "))


def show_all_students(students):
    for key, value in students.items():
        print(key, value)

rayis = Manager()

# python walrus operator
while choice := menu():
    # input -> object -> Student
    # obj -> students
    if choice == 1:
        # data = [name, age, score1, score2]
        data = input("name age score1 score2 : ").split()
        # data(esm, sen, nomre1, nomre2)
        print(rayis.add_student(name=data[0], age=data[1], score1=data[2], score2=data[3]))


    elif choice == 2:
        # show_all_students(students)
        # key_ = input("Enter a key : ")
        # data = input("name age score1 score2 : ").split()
        # students[key_] = Student(esm=data[0], sen=data[1],
        #               nomre1=data[2], nomre2=data[3])
        # print("Data updated successfully !")
        pass

    elif choice == 3:
        # show_all_students(students)
        # key_ = input("Enter a key : ")
        # students.pop(key_)
        # print("Data deleted Successfully !")
        pass

    elif choice == 4:
        # show_all_students(students)
        pass

    else:
        print("Invalid Choice !")