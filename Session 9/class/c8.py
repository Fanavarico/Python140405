n1 = {1: "A100", 2: "B200", 3: "C300"}
n2 = {1: "A150", 3: "C100", 4: "D200", 5: "E200"}
# final = {1: A250, 2: B200, 3: C400, 4: D200, 5: E200}
final = {}
key1 = set(n1.keys())
key2 = set(n2.keys())
all_keys = key1 | key2
for i in all_keys:
    # {1, 2, 3, 4, 5}
    if i in n2 and i in n1:
        adad1 = int(n1[i][1:])
        adad2 = int(n2[i][1:])
        harf = n1[i][0]
        final[i] = f"{harf}{adad1 + adad2}"
    # 2
    elif i in n1:
        final[i] = n1[i]
    # 4 5
    else:
        final[i] = n2[i]
print(final)