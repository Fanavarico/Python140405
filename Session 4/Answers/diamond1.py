import random

# way 1
secret = random.randint(1, 20)
guess = int(input("Guess the number (1-20): "))
while guess != secret:

    if guess > secret:
        print("Try a smaller number!")
    else:
        print("Try a bigger number!")
    guess = int(input("Guess the number (1-20): "))

print("🎉 Correct! The number was", secret)

# way 2
secret = random.randint(1, 20)
while True:
    guess = int(input("Guess the number (1-20): "))
    if guess == secret:
        print("🎉 Correct! The number was", secret)
        break
    elif guess > secret:
        print("Try a smaller number!")
    else:
        print("Try a bigger number!")