class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        self.speed = 0  # Initial speed

    def accelerate(self, increase):
        self.speed += increase
        print(f"{self.make} {self.model} accelerates to {self.speed} km/h")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"{self.make} {self.model} slows down to {self.speed} km/h")

# Test Car class
car1 = Car("Toyota", "Corolla", "Red")
car1.accelerate(50)
car1.brake(20)
print()