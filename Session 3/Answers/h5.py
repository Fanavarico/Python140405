# baraye posht e ham neveshtan az end = " "
# estedade mikonim ke zire ham neshon nade

num = int(input("Enter Number : "))

if 1 <= num <= 10:
    for i in range(1, num + 1):
        print(num * i, end=" ")

else:
    print("Adad beyne 1 ta 10 vared konid !")