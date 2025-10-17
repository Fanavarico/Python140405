# Game total score

# local
def qoli(pol):
    return pol + 10

# local
def hamid(geld):
    return geld + 100

# global
money = 10
qoli(money)
hamid(money)


# start Fucntion

# Scope -> local
def add_score(point):
    global score

    score += point
    print(score)


# End Fucntion

# Scope -> global
# Start main
score = 0

points = 10
score += points

points = 30
score += points

print(f"Before modify = {score}")
add_score(20)
print(f"After modify = {score}")
# End main



# grade -> erfaq(score) -> 13 -> 15


# grade -> global
# function -> score -> ++

def erfaq(score):
    global grade
    grade += score

grade = 10
erfaq(5)
print(grade)







