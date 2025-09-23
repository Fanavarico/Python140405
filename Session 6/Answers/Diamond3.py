text = input("Enter a sentence: ")
ascii_values = []

for w in text:
    ascii_values.append(ord(w))  # take ASCII of first letter

ascii_values.sort(reverse=True)
print("ASCII values high to low:", ascii_values)