file = open("odd_numbers.txt", "w")
for i in range(1, 101):   # from 1 to 100
    if i % 2 == 0:        # check even
        file.write(str(i) + "\n")  # write number + newline
file.close()
print("Odd numbers saved in odd_numbers.txt")