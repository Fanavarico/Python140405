# Read
# amir,100
# elina,200
# arshia,300
# arqavan,100
# {
# "asami": [amir, elina, ---]
# "hoqoq": [200, 300, 400, 200] + 100
# }

# file = open("karmand.txt")
# data = file.readlines()
# print(data)
# asami = []
# hoqoq = []
# for line in data:
#     # 'arshia,300\n'
#     # [arshia, 300]
#     new = line.strip().split(",")
#     print(f"new = {new}")
#     asami.append(new[0])
#     hoqoq.append(int(new[1]) + 100)
# final = {}
# final["hoqoq"] = hoqoq
# final["asami"] = asami
# print(final)
# file.close()

with open("karmand.txt") as file:
    data = file.readlines()
    print(data)
    asami = []
    hoqoq = []
    for line in data:
        # 'arshia,300\n'
        # [arshia, 300]
        new = line.strip().split(",")
        print(f"new = {new}")
        asami.append(new[0])
        hoqoq.append(int(new[1]) + 100)
    final = {}
    final["hoqoq"] = hoqoq
    final["asami"] = asami
    print(final)
