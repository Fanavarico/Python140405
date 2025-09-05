# Start function

# define
# def name(arguments):
# ---- return (meqdar)

def qoli(number):
    if number % 2 == 0:
        return number ** 2
    else:
        return "zoj nist"

# End Function

# Start Main

for i in range(1, 100):
    print(qoli(i))

# End Main