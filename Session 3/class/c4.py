# jamiat 5 keshavr migire
# oni ke az hame kamtare ro mige

# Ultra Question
# 1) kare tekrari daram ya na ? YES
# 2) kare tekrari chie ? daryaft jamiat, baresish
# 3) tekrar moshakhas ya na ? YES
# 4) for, while -> for

# # way 1
# jamiat = int(input("jamiat o bego : "))
# small = jamiat
#
# for i in range(1, 5, 1):
#     jamiat = int(input("jamiat o bego : "))
#     if jamiat < small:
#         small = jamiat
# print(small)

# # way 2
# small = 0
# for i in range(1, 6, 1):
#     jamiat = int(input("jamiat o bego : "))
#
#     if small == 0:
#         small = jamiat
#     elif jamiat < small:
#         small = jamiat
#
# print(small)

# way 3
small = 0
for i in range(1, 6, 1):
    jamiat = int(input("jamiat o bego : "))

    if small == 0 or jamiat < small:
        small = jamiat

print(small)