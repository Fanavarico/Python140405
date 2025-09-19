# students data 3
# name last_name age score
# file --> students_data.txt

total = [["amir", "amiri", 10, 10],
         ["elina", "elinayi", 20, 20]]
for data in total:
    print(data)
    temp = ""
    for mini in data:
        temp += str(mini) + ","
    temp += "\n"
    file = open("students_data.txt", "a")
    file.write(temp)
    file.close()

# way 1
# "[["amir", "amiri", 10, 10],
#  ["elina", "elinayi", 20, 20]]"

# way 2
# "["amir", "amiri", 10, 10]"
# "["elina", "elinayi", 20, 20]]"

# way 3
# "amir", "amiri", 10, 10\n