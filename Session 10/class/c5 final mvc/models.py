# file models.py : faqat khode class dakhelesh qarar migire


# Class -> Student -> name, age, score1, score2
class Student:
    # class attributes
    std_id = 1

    # Magic Method(function)
    def __init__(self, esm, sen, nomre1, nomre2):
        self.name = esm # Attributes
        self.age = sen
        self.score1 = nomre1
        self.score2 = nomre2

        self.std_id = Student.std_id
        Student.std_id += 1

    # Method
    # miangin nomarat har daneshjo
    def miangin(self):
        return (self.score1 + self.score2) / 2

    # Magic method
    # __str__
    # maqadir dakhele on ba dastor return moqe print namayesh
    # dade mishe
    def __str__(self):
        return f"Name = {self.name}, Age = {self.age}"

