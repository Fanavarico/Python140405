text = input("Enter a sentence: ")
letter = ""
i = 0
while i <= len(text):
    if i == len(text) or text[i].isspace():
        print(letter)
        letter = ""
    else:
        letter += text[i]
    i += 1