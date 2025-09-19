import time
# 1H -> 60 min

# 5H -> 1 2 3 4 5 6 7

# aqrabeye bozorg sawt
for hour in range(1, 25, 1):
    print(f"Hour = {hour}")

    # aqrabeye daqiqe shomar
    for minute in range(1, 61, 1):
        print(minute, end=" ")

    # print("Sleep 4 seconds !")
    # time.sleep(4)
