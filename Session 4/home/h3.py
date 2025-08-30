# adad begire - tamame maqsom elaih haro bege
# done done - majmoe kolesh

# 10 -> 1 2 3 4 5 6 7 8 9 10 ( % )
# 7 -> 1 2 3 4 5 6 7
# 3 -> 1 2 3
# start = 1
# stop = num
# step = 1

# total
a4 = 0


n = int(input("Enter Number : "))
for t in range(1, n + 1):
    if n % t == 0:
        print(f"Maqsom elaih = {t}")
        # print("Maqsom elaih = ", t)
        a4 += t

print(f"Adad {n} majmoe maqsom elaihash = {a4}")
# f-string -> f""
# []
# {}