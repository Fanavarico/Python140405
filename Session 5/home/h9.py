# tamami adade 2 raqami --> avale = akhar
# 11 22 33 44 55 66 -- 99
# str --> index
# shomare vagon -> 11 [0] == [1]

for k in range(10, 100):
    new = str(k)
    # 22 -> [0] -> 2
    # [1] --> 2
    # [0] == [2] --> 2 raqami
    if new[0] == new[1]:
        print(new)

# for i in range(1, 10):
#     print(str(i) * 2)