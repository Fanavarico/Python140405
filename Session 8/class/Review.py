# # Function | karmand hastand ke ma estekhdam mikonim
# # ta yek seri kar anjam bedan
#
# # jologiri az tekrar code
# # 1 bar minevisim chandbar estefade mikonim
#
# def jam(a, b):
#     return a + b
#
# hasel = jam(10, 20)
# print("Hasel = ", hasel)
#
# # List
# # vagon e qatar - data zakhire mishe
# # index dare
# # CRUD
# # Create Read Update Delete
# cars = ["C200", "XC90"]
#
# cars.append("G-Class")
# print(cars)
# # pop remove
# cars.pop(0)
# cars.remove("XC90")


# Files
# open(path, mode)
# r -> read
# w -> write - dataye qabli pak va baz nevisi mishavad
# a -> append
data = open("new.txt", "w")
data.write("p1,10\n")
data.write("p2,20\n")
data.close()

data2 = open("new.txt", "r")

# dirty -> ['p1,10\n', 'p2,20\n']
result = data2.readlines()

# clean -> [ [p1, 10], [p2, 20] ]
clean = []
for i in result:
    new =  i.strip().split(",")
    clean.append(new)
print(clean)

data.close()
# List Comprehension
# clean2 = [j.strip().split(",") for j in result]
# print(clean2)

def clean_data(data):
    clean = []
    for i in data:
        new = i.strip().split(",")
        clean.append(new)
    return clean