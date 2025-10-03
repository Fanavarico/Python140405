n1 = {"A": 100, "B": 200, "C": 300}
n2 = {"A": 101, "C": 103}
# final -> {"A": 201, "C": 403}
final = {}
for i in n1:
    if i in n2:
        final[i] = n2[i] + n1[i]
print(final)