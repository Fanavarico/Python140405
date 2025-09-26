file = open("cars.txt", "r")
lines = file.readlines()
file.close()

total_length = 0
for car in lines:
    total_length += len(car.strip())  # strip removes \n
print("Total length of all car names:", total_length)