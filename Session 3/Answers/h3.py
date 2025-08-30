num = int(input("Enter Number : "))
total = 0

for i in range(1, num, 1):
    if num % i == 0:
        print(i)
        total += 1
print("Total = ", total)
