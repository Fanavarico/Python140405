file = open("students_data.txt", "r")
data = file.readlines()
print(data)
for i in data:

    # hazfe \n ba strip
    # split bar asase ","
    new = i.strip().split(",")

    # hazfe khone khali akhare list
    # ['amir', 'amiri', '10', '10', '']
    new.pop(-1)
    print(new)

file.close()