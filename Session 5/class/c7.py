# 2 raqami ke raqame aval va akharesh yeki bashe

# Start Function

def karim(number):
    new = str(number)
    if new[0] == new[1]:
        return new
    else:
        return "no"

# End Function

# ----------------------------------------------
# ----------------------------------------------

# Start Main

for i in range(10, 100):
    result = karim(i)
    if result == "no":
        continue
    else:
        print(result)


# End Main