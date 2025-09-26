# ta karbar sefr nadade
# adad bgire to file zakhire kone
# dar akhar jamesho bege - va zakhire kone

def save_number(adad):
    file = open("numbers.txt", "a")
    file.write(str(adad) + '\n')
    file.close()

hasel = 0
adad = int(input("Enter a number : "))
while adad != 0:
    save_number(adad)
    hasel += adad
    adad = int(input("Enter a number : "))

save_number(hasel)
