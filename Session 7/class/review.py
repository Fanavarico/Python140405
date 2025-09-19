# Data Structures
# List --> sign --> [ ]
# Dictionary --> sign --> { }
# Tuple
# Set

# zakhire data va sazman dehi data
# CRUD
# Create Read Update Delete

# List

# animals -> qatar -> index --> vagon
# 0 1 2 - len()
# index -> shomare vagon ha

# Create
animals = ["babr", "mahi", "morq", "c200", "iraq", "usa"]
# Read
print(animals[1])
for k in animals:
    print(k, end=" ")
# Update
animals[3] = "shir"
print(animals)
# Delete
# remove -> value
animals.remove("iraq")
print(animals)
# pop --> index - chizi ke haz kardi ro migoft
print(animals.pop(-1))
print(animals)
