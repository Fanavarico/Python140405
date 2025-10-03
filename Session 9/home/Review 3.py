# Files -> .txt, .csv(comma separeted values)
# yek jayi baraye zakhire dat
# mode -> r, w, a
neveshte = open("karmand.txt", "r")
data = neveshte.readlines()
print(data)
neveshte.close()