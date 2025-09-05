text = "I love learning Python"
# I
# love
# learning
# python
# fasele --> didesh -> matn o bege

# 0 1 2 3 4 -- len(text)
s = 0
a4 = ""
while s <= len(text):
    print(s)
    if s == len(text) or text[s].isspace():
        print(a4)
        a4 = ""
    else:
        a4 += text[s]
    s += 1