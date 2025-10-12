import random

secret = random.randint(10, 20)
guess_count = 0

while True:
    guess = int(input("Guess the number (10-20): "))
    guess_count += 1

    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print(f"🎯 Correct! You guessed it in {guess_count} tries.")
        break