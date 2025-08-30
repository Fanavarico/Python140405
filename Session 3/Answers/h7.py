# Check if an actor's name is a palindrome
name = input("Enter an actor name: ").lower()
# Reverse the string using slicing
if name == name[::-1]: 
    print("It is a palindrome!")
else:
    print("It is not a palindrome!")