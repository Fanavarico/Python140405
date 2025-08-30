# f-string
# f" Text {variable-value} "
name = "Amir"
print(f"Seyed {name}Hosein Razavi")

# default -> for
# range(Triple S)
# start = 0
# stop = number
# step = 1
for i in range(10):
    print(i)

# break continue pass
# pass --> zamani estefade mikonim ke ye block khali
# bekhaym tarif konim
age = 20
if age > 20:
    pass
else:
    pass

# break - continue
a4 = 0
for j in range(1, 21, 1):
    # 10 XXX
    if j == 10:
        continue
    elif j == 15:
        break
    a4 += j
    print(f"Adad {j}")
print(a4)

# ASCII
# American Standard Code for Information Interchange
# string method -> lower - upper - space - swapcase ---
# 1) chejori az ascii ha toye python estefade mikonan
# 2) chejori man tamame horofe kochik alefbaro neshon bedam
# 65 - 122

# ord -> adade marbot be harfaro mige - code ascii ro mige
print(ord("A"))
# chr -> code ascii ro be harf tabdil mikone
print(chr(65))

for word in range(65, 123):
    if 91 <= word <= 96:
        continue
    else:
        # print(end="\n")
        # \n -> new line
        # \t -> tab
        print(f"word = {chr(word)}", end=" ")



# one line input
# library