# Default arguments - erfaqe nomre
def erfaqe_nomre(nomre, erfaq=5):
    return nomre + erfaq


print(erfaqe_nomre(10, 1))


# Positional arguments - greet
def greet(name, last_name):
    print(f"Hello {name} {last_name}")

# greet("amir", "razavi")
greet("razavi", "amir")

# Keyword arguments - 0 ta 100 mashin
def car_speed(start, stop):
    print(f"Car speed strarted at {start} and reach {stop}")

car_speed(start=0, stop=100)