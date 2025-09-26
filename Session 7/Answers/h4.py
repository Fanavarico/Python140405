file = open("countries.txt", "r")
lines = file.readlines()
file.close()

total = 0
for line in lines:
    data = line.strip().split(",")   # split into [country, population]
    population = int(data[1])
    total += population

print("Total population:", total)