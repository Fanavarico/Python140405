# Class name standard
# CamelCase -> StudentManagementClass

# Blueprint
class Car:

    # Magic method | Dunder Method (Double Underline Methods)
    def __init__(self, modelesh, soratesh, rangesh):
        self.model = modelesh # Attribute | Property
        self.speed = soratesh
        self.color = rangesh

    # Method (functions)
    def horn(self):
        print("booq !")

# object | instance
benz = Car("c200", 200, "black")
print(benz.speed) # dot notation
print(benz.color)