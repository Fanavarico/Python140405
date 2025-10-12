text = input("Enter a text: ").lower()
letters = {}

for ch in text:
    if ch.isalpha():  # only count letters
        if ch in letters:
            letters[ch] += 1
        else:
            letters[ch] = 1

print(letters)