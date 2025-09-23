secret = [3, 7, 9]
for i in range(5):
    guess = int(input("Guess a number between 1-10: "))
    if guess in secret:
        print("Correct! Removing from list...")
        secret.remove(guess)
    else:
        print("Wrong guess!")
print("Game over! Numbers left:", secret)