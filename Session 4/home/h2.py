# Adad begire bege avale ya nist
# 13 - 2 - 7 - 5
# maqsom elaih -> nadare - 2 (1, khodesh)

# way 1
# faqat 2 ta dasht bashe
# 7 -> 1, 7 --> 2

# way 2
# be hichi bakhsh pazir nabashe
# 7 -> 2 - 6 --> 0

number = int(input("Enter Your Number : "))

# Ultra Question
# 1) kare tekrari darim ya na ? YES
# 2) kare tekrari chie ? mohasebe baqimande - jame tedadesh
# 3) tekrar moshakhas ya na ? YES
# 4) for, while -> for

# shomaresh adad ha
a4 = 0

# 7 -> 2 3 4 5 6
# 10 -> 2 3 4 5 6 7 8 9
for i in range(2, number, 1):
    if number % i == 0:
        a4 += 1

if a4 == 0:
    print("Aval Ast !")
else:
    print("Aval nist !!!")