# Inheritance
class Human:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

class Student(Human):
    def __init__(self, name, last_name, age, score):
        super().__init__(name, last_name, age) # Father class
        self.score = score

    def __str__(self):
        return f"Student | name = {self.name} | last name = {self.last_name} | age = {self.age} | score = {self.score}"

class Teacher(Human):
    def __init__(self, name, last_name, age, salary):
        super().__init__(name, last_name, age) # Father class
        self.salary = salary

    def __str__(self):
        return f"Teacher | name = {self.name} | last name = {self.last_name} | age = {self.age} | salary = {self.salary}"

s1 = Student("amir", "razavi", 10, 20)
print(s1)

t1 = Teacher("elina", "mnejad", 20, 1000)
print(t1)

# Polymorphism
class Father:
    def cooler(self):
        print("Khamosh mikonam coolero | hava khobe")

class Mother:
    def tanbih(self):
        print("Dampayi !!")

class Child(Father, Mother):
    def cooler(self):
        print("man khamoshesh nemikonam")

    def tanbih(self):
        print("pol to jibi behet nemidam !")

farzand = Child()
farzand.tanbih()
farzand.cooler()



# Encapsulation

class BankAccount:
    # method --> getter, setter
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        self.__balance -= money

    def __str__(self):
        return f"Balance is = {self.__balance}"


person1 = BankAccount("Amir", 10000)
print(person1.owner)
person1.deposit(1000)
print(person1)
person1.withdraw(11000)
# Access private attribute from out side of the class
print("out of class", person1._BankAccount__balance)
# Abstraction

from abc import ABC, abstractmethod
# AbstractBaseClass

class Car(ABC):

    @abstractmethod
    def start(self):
        pass

class ElectronicCar(Car):
    def start(self):
        print("Starting a electronic car !")

class DieselCar(Car):
    def start(self):
        print("Starting a diesel car !")

e1 = ElectronicCar()
e1.start()
d1 = DieselCar()
d1.start()
