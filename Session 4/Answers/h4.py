sea = input("Enter the name of a sea or ocean: ")
biggest = sea[0]  # assume first letter is biggest
for ch in sea:
    if ord(ch) > ord(biggest):   # compare ASCII codes
        biggest = ch
print("The biggest ASCII character is:", biggest)