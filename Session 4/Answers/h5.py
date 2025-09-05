total = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if num == 100:
        break   # stop immediately if 100 found
    total += num
print("The total before 100 is:", total)