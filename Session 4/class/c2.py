# kare lower ro anjam bede
text = "I LoVE LearNIng Python"
a4 = ""

# Big -> 65 - 90
# Small -> 97 - 122
# difference -> 32
for word in text:
    # A -> 65
    number = ord(word) # tabdil harf be adad kardim
    # baresi kardim
    # 65 - 90 -> BIG
    if 65 <= number <= 90:
        small = number + 32
        a4 += chr(small)
    else:
        a4 += word

print(a4)
