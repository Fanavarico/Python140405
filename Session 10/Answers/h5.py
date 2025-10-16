class Human:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def full_name(self):
        print(f"Full name: {self.name} {self.family}")

    def show_age(self):
        print(f"Age: {self.age}")

# Test Human
human1 = Human("John", "Doe", 25)
human1.full_name()
human1.show_age()
print()