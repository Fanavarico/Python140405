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
# [std1, std2, std3]
# object -> Student

students = {}
# {"std1": obj, "std2": obj}
shomare = 1
# python walrus operator
while choice := menu():
    # input -> object -> Student
    # obj -> students
    if choice == 1:
        # data = [name, age, score1, score2]
        data = input("name age score1 score2 : ").split()
        # data(esm, sen, nomre1, nomre2)

        # data(amir, 20, 20, 20)
        # data(esm=amir, sen=20, nomre1=20, nomre2=20)
        std = Student(esm=data[0], sen=data[1],
                      nomre1=data[2], nomre2=data[3])

        students[f"std{shomare}"] = std
        shomare += 1


    elif choice == 2:
        show_all_students(students)
        key_ = input("Enter a key : ")
        data = input("name age score1 score2 : ").split()
        students[key_] = Student(esm=data[0], sen=data[1],
                      nomre1=data[2], nomre2=data[3])
        print("Data updated successfully !")

    elif choice == 3:
        show_all_students(students)
        key_ = input("Enter a key : ")
        students.pop(key_)
        print("Data deleted Successfully !")

    elif choice == 4:
        show_all_students(students)


    else:
        print("Invalid Choice !")