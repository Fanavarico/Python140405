# CRUD + menu

# Error

# Error handling block
# try
# except
# else
# finally

# TypeError
try:
    print(1 + 1)
    a = [1]
    print(a[10])
except TypeError as e:
    print("Fekr mikonam ke int o ba str dari jam mikoni", e)
except IndexError as e :
    print("Other errors !", e)
else:
    print("No Error !")
finally:
    print("Im running any way :)")

#
# # IndexError
# a = []
# try:
#     print(a[10])
# except:
#     print("After IndexError")







































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
    try:
        choice = int(input("Enter Your Choice : "))

    except ValueError:
        print("eshtebah gozine dadi ")

    else:
        return choice

def elina_read_data(data):
    for std in data:
        print(std)

# End Function

# Start Main

choice = amir_menu()
total = []

while choice != 0:

    if choice == 1:
        student_data = input("Name Last_name Age Score : ").split()
        total.append(student_data)

    elif choice == 2:
        elina_read_data(total)
        try:
            index_user = int(input("Enter an index : "))
            student_data = input("Name Last_name Age Score : ").split()
            total[index_user] = student_data
        except IndexError:
            print("index eshtebah dadi !")


    elif choice == 3:
        elina_read_data(total)
        index_user = int(input("Enter an index : "))
        print("deleted data = ", total.pop(index_user))

    elif choice == 4:
        elina_read_data(total)

    else:
        print("Invalid Choice !")

    choice = amir_menu()

# End Main



















# print(x)  # NameError: name 'x' is not defined

# x = "5"
# y = 10
# print(x + y)  # TypeError: can only concatenate str (not "int") to str

# lst = [1, 2, 3]
# print(lst[5])  # IndexError: list index out of range

# d = {"name": "Alice"}
# print(d["age"])  # KeyError: 'age'

# x = 10
# x.append(5)  # AttributeError: 'int' object has no attribute 'append'

# int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'

# x = 10 / 0  # ZeroDivisionError

# import maths  # ImportError: No module named 'maths'

# f = open("nonexistent.txt")  # FileNotFoundError

# lst = []
# print(lst.pop())  # IndexError at runtime

# try:
#     x = int("abc")
# except ValueError as e:
#     print("Caught an error:", e)
#
# try:
#     y = 10 / 0
# except ZeroDivisionError as e:
#     print("Caught an error:", e)