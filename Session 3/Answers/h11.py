# Analyze text: vowels, uppercase, lowercase, spaces, special signs, numbers
text = input("Enter a long line of text: ")

count_vowel = 0
count_upper = 0
count_lower = 0
count_spaces = 0
count_special = 0
count_numbers = 0

vowels = "aeiou"

for ch in text:
    if ch.lower() in vowels:  # check if it is a vowel
        count_vowel += 1
    if ch.isupper():
        count_upper += 1
    elif ch.islower():
        count_lower += 1
    elif ch.isspace():
        count_spaces += 1
    elif ch.isdigit():
        count_numbers += 1
    else:
        count_special += 1

print("Vowels:", count_vowel)
print("Uppercase:", count_upper)
print("Lowercase:", count_lower)
print("Spaces:", count_spaces)
print("Numbers:", count_numbers)
print("Special characters:", count_special)