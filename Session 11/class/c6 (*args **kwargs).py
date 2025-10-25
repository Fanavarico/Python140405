# *args -> student average score
def average_score(*args):
    print(args, sum(args)/ len(args))

average_score(10, 20, 30, 10, 20, 10)


# **kwargs -> student profile with different info - name **kwargs
def student_profile(**kwargs):
    total.append(kwargs)
    print(kwargs, type(kwargs))

total = []
student_profile(name="amir", phone="0912", age=15)
print(total)
student_profile(name="elina", phone="0912", age=15, salary=1000)
print(total)
