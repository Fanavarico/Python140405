# Loops
# for -> moayan - moshakhas
# Syntax
# for variable in iterable
# iterable :
# range
# str
# list
# dict
# set
# tuple
# ....

# iterate -> amale peymayesh
# iterable -> khode mohite qabele peymayesh

# Triple S -> Start, Stop, Step
for i in range(1, 10, 1):
    print(i)


# while -> na moayan va na moshakhas
s = 10
while s != 0:
    print("salam")
    s -= 1


# data structure
# list
# indexing -> 0 1 2 -- len()
# 0 1
# Create
persons = ["p1", "p2"]
# Read
print(persons)
# Update
persons[0] = 1
# Delete
persons.remove("p2")
persons.pop(0)

# dict
# index -> X
# key: value

# Create
countries = {"iran": 100, "usa": 300, "germany": 80}
# Read
print(countries)
for key, value in countries.items():
    print(key, value)
# Update
countries["iran"] = 0
# Delete
countries.pop("germany")

# set
data = {1, 2, 3, 4, 5, 1, 2, 3, 4, 10, "bmw", "benz"}

# tuple
id_ = ("002211111",1, 2)
# Unpack
a, b, c = id_
a = "001"

# Pack
id_ = (a, b, c)