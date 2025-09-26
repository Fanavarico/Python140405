cars = {"car1": [22, 33 ,44 ,55],
        "car2": [11, 22 , 33 ,44]}
print(cars)

print(list(cars.keys()))
print(list(cars.values()))
print(list(cars.items()))
# ('car1', [22, 33, 44, 55]), ('car2', [11, 22, 33, 44])
name, last_name = ("amir", "razavi")
for key, value in cars.items():
    print(key, value)
