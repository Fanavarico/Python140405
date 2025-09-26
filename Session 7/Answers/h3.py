file = open("users.txt", "w")
for i in range(5):
    name = input("Enter username: ")
    score = input("Enter score: ")
    file.write(name + "," + score + "\n")
file.close()
print("Users and scores saved in users.txt")