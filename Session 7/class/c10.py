# esm 5 ta kesvar ro zakhire kon dakhele file
# country.txt

for _ in range(5):
    country = input("Enter country : ")
    file = open("country.txt", "a")
    file.write(country + "\n")
    file.close()