username = input("Enter username : ")
# password = int(input("Enter Password : ")) 0912 -> 912
password = input("Enter Password : ")


# SyntaxError: leading zeros in decimal integer literals are not permitted;
# use an 0o prefix for octal integers
# if username == "amir" and password == 0912:
if username == "amir" and password == "0912":
    print("Welcome !")
else:
    print("Not Welcome !")