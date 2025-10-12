factorials = {}

for n in range(10, 21):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    factorials[n] = fact

print(factorials)