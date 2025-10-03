# Tuples in python
# Tuple is a collection which is ordered and unchangeable.
# Allows duplicate members.
# sign -> (1, 2, 3)
# data mohem dakhele tuple zakhire mishe

ids = (1, )
id2 = 2,
print(type(ids))
id2 = 2,
print(f"Type id 2 {type(id2)}")

# CRUD

# Create
salary = (100, 200, 300)
# Read
print(salary)
print(type(salary))
# Update -> X
# print(salary[1])
# for i in salary:
#     print(i)
# salary[0] = 900
# Delete -> X
# salary.pop(0)
# salary.remove(100)

# Unpack
# s1, s2, s3 = (100, 200, 300)
s1, s2, s3 = salary
print(s1)
print(s2)
print(s3)
s1 += 400
s2 += 300
s3 -= 200
# Pack
salary = (s1, s2, s3)
print(f"Salary = {salary}")

new = ( {"name": "amir", "last_name": "razavi"},
        [10, 20, 10, 15],
        10, 11, 22, 33, 11 )
print(new[1])
print(tuple([10, 20, 10, 15]))