# Set in python
# sign = { value, value2 }
# Set is a collection which is unordered, unchangeable*,
# and unindexed. No duplicate members.

speed = {100, 200, "iran",100, 200, 300, "amir", "bmw"}
print(speed)
print(type(speed))

m1 = {100, 200, 300, 400}
m2 = {200, 300}
print(m1.difference(m2))
print(f"intersection = {m1.intersection(m2)}")
print(f"issubset = {m2.issubset(m1)}")
print(m1 | m2)

# CRUD
# Create
m1 = {100, 200, 300, 400}
m2 = {200, 300}
# Read
print(m1)
print(m2)
# Index -> X
# print(m1[0])
# loop -> OK
for i in m1:
    print(i)
# Update -> set of collections
m2.update({10, 20})
m2.add("amir")
# Delete
m2.remove("amir")
# discard -> age vojod nadasht on value -> Error nemide
print(m2.discard(200))
