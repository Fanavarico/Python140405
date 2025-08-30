# adad ro str migirim va rosh peymayesh mikonim va harbar
# ke khastim estefadash konim be int tabdil mikonim


num = input("Enter Number : ")
total = 0

for i in num:
    total += int(i)

if int(num) % total == 0:
    print("Adade = ", num, "bar majmoe arqam baksh pazir ast !", total)
else:
    print("Adade = ", num, "bar majmoe arqam baksh pazir nits !!!", total)
