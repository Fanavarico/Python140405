# MVC -> Design Pattern

# Model -> class
# View -> UI / input-print / tkinter / web
# Controller -> CRUD - database - read

# Classes
# Blueprint
# CamelCase
# data + functionality
class Car: # Blueprint
    # Constructor
    # Magic Method | Dunder Method
    def __init__(self, esm, rang, sorat=0):
        self.name = esm
        self.rang = rang
        # self.speed = 0
        self.speed = sorat

    # 10 - 100 - 50
    def increase_speed(self, new_speed):
        self.speed += new_speed

    # break
    # sorate delkhah begir
    # az ser kamtar nashe
    def decrease_speed(self, new_speed):
        if new_speed <= self.speed:
            self.speed -= new_speed
        else:
            print("Invalid Speed")


    # print -> che matni neshon bedam
    def __str__(self):
        return f"{self.name} , speed = {self.speed}"

# Library
# Human -> attributes -> name, last_name, id, age
# methods -> qarz_gereftan, pas_dadan, sabte_nam

# Book -> attributes -> name, title, author, color, category
# method ->

# object | instance
benz = Car("s500", "black")
benz.increase_speed(100)
benz.decrease_speed(50)
benz.decrease_speed(50)
benz.decrease_speed(50)
print(f"Benz = {benz}")
bmw = Car("M5", "blue")



print(f"Benz = {bmw}")