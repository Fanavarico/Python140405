# Count how many times 'a', 'z', and 't' appear in a text
text = input("Enter a text: ")

count_a = 0
count_z = 0
count_t = 0

for ch in text:  # go through each character
    if ch.lower() == 'a':
        count_a += 1
    elif ch.lower() == 'z':
        count_z += 1
    elif ch.lower() == 't':
        count_t += 1

print("Number of 'a':", count_a)
print("Number of 'z':", count_z)
print("Number of 't':", count_t)