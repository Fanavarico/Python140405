# 🦁 Zoo Management System

# Class Definitions
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} | {self.species} | {self.age} years old"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def update_animal(self, index, animal):
        self.animals[index] = animal

    def delete_animal(self, index):
        return self.animals.pop(index)

    def show_animals(self):
        for i, a in enumerate(self.animals):
            print(f"{i} - {a}")


# Menu Functions
def zoo_menu():
    print("1| Add Animal")
    print("2| Update Animal")
    print("3| Delete Animal")
    print("4| Show Animals")
    print("0| Exit")


# Main Program
zoo = Zoo()

zoo_menu()
choice = int(input("Enter Your Choice: "))

while choice != 0:
    if choice == 1:
        data = input("Name Species Age : ").split()
        a = Animal(data[0], data[1], data[2])
        zoo.add_animal(a)

    elif choice == 2:
        zoo.show_animals()
        index = int(input("Enter index to update: "))
        data = input("Name Species Age : ").split()
        a = Animal(data[0], data[1], data[2])
        zoo.update_animal(index, a)

    elif choice == 3:
        zoo.show_animals()
        index = int(input("Enter index to delete: "))
        print("Deleted:", zoo.delete_animal(index))

    elif choice == 4:
        zoo.show_animals()

    else:
        print("Invalid Choice!")

    zoo_menu()
    choice = int(input("Enter Your Choice: "))