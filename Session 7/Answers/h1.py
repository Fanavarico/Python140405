words = []
for i in range(10):
    word = input("Enter a word: ")
    words.append(word + "\n")   # add newline for each word

file = open("words.txt", "w")   # open file for writing
file.writelines(words)          # write all words at once
file.close()
print("Words saved in words.txt")