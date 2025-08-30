# adad bgire beyne 1 - 10 -> jadval zarb 1 - 10 neshon bede
# num --> 1 - 10
# num * 1
# num * 2
# ---
# num * 10
from dataclasses import asdict

op = int(input("Enter Adad : "))
if 1 <= op <= 10:
    for kk in range(1, 11, 1):
        # print(op * kk)
        # 1 -> 1 * 3 = 3
        print(f"{kk} -> {kk} x {op} = {op * kk}")
else:
    print("Invalid Number !")
