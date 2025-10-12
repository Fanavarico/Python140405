total = 0
count = 0
names = []

with open("students.txt", "r") as file:
    for line in file:
        name, score = line.split()
        names.append(name)
        total += float(score)
        count += 1

average = total / count
print("Students:", names)
print("Average score:", average)