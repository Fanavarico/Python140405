from functions import clean_data_without_split
# tole kole reshteha cheqade
# 206 + 405 -> 6

jameshon = 0
total = open("cars.txt")
data = total.readlines()
clean = clean_data_without_split(data)
for i in clean:
    jameshon += len(i)

total.close()
print(jameshon)