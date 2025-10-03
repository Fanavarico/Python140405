n1 = {1: "A100", 2: "B200", 3: "C300"}
n2 = {1: "A150", 3: "C100", 4: "D200", 5: "E200"}
# final = {1: A250, 3: C400}
final = {}
for avali in n1:
    if avali in n2:
        # n1[avali] -> "A100"
        adad1 = int(n1[avali][1:])
        adad2 = int(n2[avali][1:])
        harf = n1[avali][0]
        final[avali] = f"{harf}{adad1 + adad2}"
print(final)