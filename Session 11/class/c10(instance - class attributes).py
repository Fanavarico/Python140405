class Car:
    # class attributes
    total_created_cars = 0
    doors = 4
    wheels = 4

    def __init__(self, esm, rang, sorat=0):
        self.name = esm # instance attribute
        self.color = rang
        # self.speed = 0
        self.speed = sorat
        Car.total_created_cars += 1

    def increase_speed(self, new_speed):
        self.speed += new_speed

    def decrease_speed(self, new_speed):
        if new_speed <= self.speed:
            self.speed -= new_speed
        else:
            print("Invalid Speed")

    def __str__(self):
        return f"{self.name} , color = {self.color},speed = {self.speed}"

kia = Car("cerato", "red", 200)
kia.doors = 2
print(kia, f"doors {kia.doors} | wheels = {kia.wheels}")
print(kia.total_created_cars)

volvo = Car("XC90", "Black", 200)
print(volvo, f"doors {volvo.doors} | wheels = {volvo.wheels}")
print(volvo.total_created_cars)

saipa = Car("pride", "red", 90)
print(saipa, f"doors {saipa.doors} | wheels = {saipa.wheels}")
print(saipa.total_created_cars)
