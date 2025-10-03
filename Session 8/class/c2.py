# List -> sign -> [ ]
# Dictionary -> sign -> { }
# key: value
# index -> X
# keys
std1 = { "name": "amir hosein", "last_name": "razavi",
         "height": 190, "weight": 90 }

# for i in std1:
#     print(i)

print(std1["height"])

# { name: [], last_name: [] }
# animals :
# vahshi -> [ shir, babr ]
# ahli -> [ morq - khoros ]
# total -> 2
# 101 -> "2 daste bandi darim"
# 007 -> "ranande"
animals = {
           "vahshi": ["shir", "babr"],
           "ahli": ["morq", "khoros"],
           "total": 2,
           101: "2 daste bandi darim",
           "007": "ranande",
           "ahli": ["mahi", "gorbe", ["khers"]]
           }

print(animals)
print(animals[101])
# animals["ahli"] -> ["mahi", "gorbe", ["khers"]]
# index -> 2 -> ["khers"]
print(animals["ahli"][2][0])