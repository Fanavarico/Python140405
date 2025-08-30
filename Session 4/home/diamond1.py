# data 7 karmand o begir
# hoqoq, male, female
# tedad -> female, male
# miangin hoqoqe -> male, female

# Algorithm
male = 0
female = 0
salary_m = 0
salary_f = 0

# 1 2 3 4 5 6 7
# esm variable estefade nemishe tarif nakon
# underline -> estefade nemishe
for _ in range(1, 3, 1):
    # 0 -> male , 1 -> female
    # female male
    # f m
    male_or_female = input("Male / Female : ") # Female - FemAle - female
    salary = float(input("Enter Your salary : "))
    if male_or_female.lower() == "male":
        male += 1
        salary_m += salary
    elif male_or_female.lower() == "female":
        female += 1
        salary_f += salary

print(f"Total men = {male}")
print(f"Total women = {female}")
print(f"Average men = {salary_m / male}")
print(f"Average women = {salary_f / female}")
print("Error Zero !")

