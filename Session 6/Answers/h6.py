singers = ["Ariana", "Rihanna", "Selena", "Drake", "Bieber"]
new_list = []
for s in singers:
    if "R" not in s.upper():
        new_list.append(s)
print("Singers without R:", new_list)