from pprint import pprint
# range -> 1 - 100
# total = { "zoj": [],
#           "fard": []}

# Version 1
# fard = []
# zoj = []
# for adad in range(1, 100):
#     if adad % 2 == 0:
#         zoj.append(adad)
#     else:
#         fard.append(adad)
#
# total = {}
# total["zoj"] = zoj
# total["fard"] = fard
# print(total)
# pprint(total)
# Syntax adding -> variable[key] = value

# Version 2
# List Comprehension
# fard = [i for i in range(1, 100) if i % 2 != 0]
# zoj = [i for i in range(1, 100) if i % 2 == 0]
# total = {}
# total["zoj"] = zoj
# total["fard"] = fard
# print(total)

# Version 3
# Dictionary Comprehension
total = {
    "fard": [i for i in range(1, 100) if i % 2 != 0],
    "zoj": [i for i in range(1, 100) if i % 2 == 0]
}
print(total)