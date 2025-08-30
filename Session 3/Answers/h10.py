# Show the word "PYTHON" in a diagonal pattern
word = "PYTHON"
for i in range(len(word)):
    # print spaces first, then the letter
    print(" " * i + word[i])