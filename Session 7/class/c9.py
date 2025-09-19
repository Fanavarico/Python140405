# files
# .txt - .csv (comma separated values)
# amir,hasan,mobina,reza

# open(path, mode)
# mode
# r -> read
# w -> write (data az qable zakhire shode pak mishe)
# a -> append

file = open("first.txt", "w")
file.write("amir hosein razavi\n")
file.write("reza rezayi\n")
file.close()

file2 = open("first.txt", "r")
data = file2.readlines()
print(data)
file2.close()