# built-in Library
# Syntax -> import library
import time
import playsound3
# Download Libray syntax -> pip isntall name
# terminal


# While
# Loop -> for
# Loop -> While
# while -> condition

# Transfer -> for be while

# start = 1
# ta zamani ke be 11 naresidi
# jam kone ba adade 1
# be 11 residi edame nade

# for i in range(1, 11, 1):
#     print(i)



# 10 - 0 Boom

# start
n = 5
print("Bomb Planted !")
print("You have 5 Second to decide !")
print("Which wire to cut : White, Red, Yellow")
playsound3.playsound("bomb_planted.mp3")
# stop
while n != -1:
    print(n)
    playsound3.playsound("beep.mp3")
    # library.method()
    time.sleep(1)
    # step
    n -= 1
question = input("Choose one : White, Red, Yellow").lower()
if question == "red":
    print("Boom !")
else:
    print("You Saved Us !")

# random
