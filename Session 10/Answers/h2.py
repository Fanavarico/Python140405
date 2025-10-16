class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof Woof!")

    def eat(self, food):
        print(f"{self.name} eats {food}")

# Test Dog class
dog1 = Dog("Max", "Bulldog", 3)
dog1.bark()
dog1.eat("meat")
print()