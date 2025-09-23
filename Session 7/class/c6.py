# jadval zarb
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 ---
# 3 6 9 ----
# 4 ----
# nested for

for i in range(1, 11 ,1):
    # 1
    for j in range(1, 11, 1):
        # 1 2 3 4 5 6 7 8 9 10
        print(i * j, end="\t")
    print()