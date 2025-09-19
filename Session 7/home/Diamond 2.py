number = [1, 2, 3, 1, 2, 3, 7]
# single -> 7
for i in number:
    # print(f"{i} = {number.count(i)}")
    if number.count(i) == 1:
        print(i)
