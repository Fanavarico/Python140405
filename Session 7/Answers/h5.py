file = open("numbers.txt", "a")

total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
    file.write(str(num) + "\n")

file.write("Sum=" + str(total) + "\n")
file.close()
print("Numbers and sum saved in numbers.txt")