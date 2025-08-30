# avalin mashin ham kochik tarin hast va ham bozorg tarin
# chon qablesh chizi baraye moqayese nist va avalin mashin
# hast ke daryaf mikonim
car_power = int(input("Enter Car Power : "))
small = car_power
big = car_power
total = car_power

for i in range(1, 7, 1):
    car_power = int(input("Enter Car Power : "))
    if car_power > big:
        big = car_power
    elif car_power < small:
        small = car_power
    total += car_power

print("Big = ", big)
print("Small = ", small)
print("Total = ", total)
print("Average = ", total / 6)