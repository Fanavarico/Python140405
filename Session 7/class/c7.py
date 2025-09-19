# 5
# * 1
# ** 2
# ** 2
# *** 3
# *** 3
# **** 4
# **** 4
# ***** 5
# ***** 5
# ****** 6

# Way 1
for i in range(1, 6, 1):
    # 1
    # 2 **
    print(i*"*")
    for j in range(1, i + 2):
        # 1 2 3
        print("*", end="")
    print()

# # Way 2
# a = "*"
# for i in range(1, 6, 1):
#     result = a * i
#     print(result)
#     for j in range(1, 2, 1):
#         if i != 1:
#             print(result)

# # Way 3
# for i in range(1, 6, 1):
#     if i == 1:
#         print("*")
#     else:
#         print("*" * i)
#         print("*" * i)