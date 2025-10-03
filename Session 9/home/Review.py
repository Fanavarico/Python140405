# List --> [ ]
# CRUD

# Create
animals = ["shir", "morq"]
# Read
print(animals)
for i in animals:
    print(i)
# Update
animals[1] = "babr"
print(f"After update {animals}")
# ['shir', 'babr']
# Delete
animals.pop(0)
animals.remove("babr")
print(animals)


# Dictionary --> {key: value}
# CRUD
# Create
cars = {"car1": "bmw",
        "car2": "benz"}
# Read
print(cars)
for j in cars:
    print(cars[j])

print(cars.keys())
print(list(cars.values()))

for key, value in cars.items():
    print(key, value)
# Delete
cars.pop("car1")
print(f"After delete {cars}")
# Update
cars["car3"] = "pride"
print(cars)