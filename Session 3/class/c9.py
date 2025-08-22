text = "I Love Learning Python3 in 50+10 Hours."

# tedad :
# bozorg -> 10
# kochik -> 3
# space -> 6
# adad -> 2
# +. -> 2

bozorg = 0
kochik = 0
space = 0
adad = 0
alamat = 0

for word in text:
    if word.isupper() == True:
        # bozorg = bozorg + 1
        bozorg += 1
    elif word.islower() == True:
        kochik += 1
    elif word.isspace() == True:
        space += 1
    elif word.isdigit() == True:
        adad += 1
    else:
        alamat += 1

print("bozorg = ", bozorg)
print("kochik = ", kochik)
print("space = ", space)
print("adad = ", adad)
print("alamat = ", alamat)
