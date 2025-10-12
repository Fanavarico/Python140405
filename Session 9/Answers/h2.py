text = input("Enter a sentence: ")
words = text.split()
ascii_dict = {}

for word in words:
    total = 0
    for ch in word:
        total += ord(ch)
    ascii_dict[word] = total

print(ascii_dict)