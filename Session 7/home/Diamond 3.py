# matn begire -> code ascii ro zakhire kone
# az bozorge be kochik moratab kone

total = []
text = "Hello im LearNIng PYThon"
# ord
print(ord("A"))
for i in text:
    total.append(ord(i))
print(total)
total.sort(reverse=True)
print(total)