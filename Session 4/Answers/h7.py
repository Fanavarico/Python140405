# way 1
for i in range(10, 100, 1):
    number = str(i)
    if number[0] == number[1]:
        print(i)

# way 2
for i in range(1, 10):
    print(str(i) * 2)