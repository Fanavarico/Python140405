# Syntax
# class name
# CamelCase
# student_management_class
# StudentManagementClass



# Blueprint
class Car:
    # dunder methods
    # double underlin --> dunder
    # magic methods

    # Method -> hamon functions
    # init -> magical(dunder) method -> __init__
    # Constructor |Initializer
    # sazande
    def __init__(self, modelesh, soratesh, rangesh):
        self.model = modelesh # Attributes
        self.speed = soratesh
        self.color = rangesh


# representation
# __repr__

# object | instance
benz = Car("c200", 200, "black")
print(benz.speed) # dot notation
print(benz.color)


# bmw = Car()
# bmw.model = "i8"
# bmw.speed = 180
# bmw.color = "blue"
#
# # Volvo
# volvo = Car()
# volvo.model = "XC90"
# volvo.speed = 200
# volvo.color = "gray"

# print(f"benz = {benz}")
# print(f"bmw = {bmw}")
# print(f"volvo = {volvo}")