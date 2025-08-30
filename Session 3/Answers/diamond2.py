# Employee statistics: men vs women and average salaries
count_men = 0
count_women = 0
sum_men_salary = 0
sum_women_salary = 0

for i in range(7):  # for 7 employees
    gender = input(f"Enter gender of employee {i+1} (M/W): ").lower()
    salary = float(input(f"Enter salary of employee {i+1}: "))

    if gender == "m":
        count_men += 1
        sum_men_salary += salary
    elif gender == "w":
        count_women += 1
        sum_women_salary += salary
    else:
        print("Invalid gender entered, skipping...")

avg_men = sum_men_salary / count_men
avg_women = sum_women_salary / count_women

print("Total Men:", count_men)
print("Total Women:", count_women)
print("Average Salary of Men:", avg_men)
print("Average Salary of Women:", avg_women)