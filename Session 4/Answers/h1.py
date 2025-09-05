count = 0
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    num = int(input("Enter a number (0 to stop): "))
    count += 1     # add 1 to the count for each number
print(f"You entered {count} numbers.")
