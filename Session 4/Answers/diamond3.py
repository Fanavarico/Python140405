import time
import random

print("Get ready! You will see 5 numbers in 3 seconds. Type them quickly!")
total_time = 0
time.sleep(3)

for _ in range(5):
    num = random.randint(100, 1000)   # random 100 – 1000
    print("Type this number:", num)
    start = time.time()          # start timing
    guess = int(input("Your answer: "))
    end = time.time()            # end timing

    if guess == num:
        reaction = end - start   # calculate how long it took
        total_time += reaction
    else:
        print("Wrong! Try to be careful.")

print("Your total time for 5 numbers is:", round(total_time, 2), "seconds")