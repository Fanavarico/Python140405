# List
# sign --> [ ]
# Data Structures
# List - Dictionary - Tuple - Set
n1 = [1, 2, 3]
print(type(n1))

country = "iran usa germany"

# 0 1 2 3 --  -2 -1
# string

# index
animal_train = ["shir", "morq", "mahi"]
print(animal_train)
print(animal_train[0])
print(animal_train[-1])
# slice
print(animal_train[0: 2])

for i in animal_train:
    print(i)

print("len = ", len(animal_train))

# 5 ta esm heyvanat ro begire
# va dakhele yek list zakhire va namayesh bede
# List Methods
# a1 = input("Enter Animal : ")
# a2 = input("Enter Animal : ")
# a3 = input("Enter Animal : ")
# a4 = input("Enter Animal : ")
# a5 = input("Enter Animal : ")
# animals = [a1, a2, a3, a4, a5]
# heyvanat = []
#
# for _ in range(5):
#     animal = input("Enter A animal name : ")
#     heyvanat.append(animal)
#
# print(heyvanat)

# CRUD -> Create Read Update Delete

# Create
heyvanat = []
#
# for _ in range(5):
#     animal = input("Enter A animal name : ")
#     heyvanat.append(animal)

# Read
print(heyvanat)

# Update
# geman --> germany
# variable = value
country = ["iran", "iraq", "dubai", "geman"]
# variable[index] = new value
country[3] = "germany"
print(country)

# Delete
cars = ["C200", "G-Class", "XC90", "kawazaki", "CB-1000"]

# remove -> value
result = cars.remove("kawazaki")
print(cars)
print(f"result remove {result}")
# pop -> index
result2 = cars.pop(3)
print(cars)
print(f"result pop {result2}")

# CRUD
# Create
animals = ["babr", "palang", "mahi"]
# Read
print(animals)
# Update
animals[0] = "shir"
# Delete
animals.remove("mahi")
animals.pop(0)
print(animals.index("palang"))