list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
common = []
for n in list1:
    if n in list2:
        common.append(n)
print("Common numbers:", common)