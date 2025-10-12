A = [1, 2, 3, 5]
B = [1, 3, 6, 7]

unique = []

# First, take numbers from A that are not in B
for num in A:
    if num not in B:
        unique.append(num)

# Then, take numbers from B that are not in A
for num in B:
    if num not in A:
        unique.append(num)

print("Unique numbers:", unique)