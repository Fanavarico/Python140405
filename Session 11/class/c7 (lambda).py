# lambda arguments: return
# def add(a, b):
#     return a + b

add = lambda a,b: a + b
print(add(10, 20))



def multiply(a, b):
    return a * b

b = lambda a,b: a * b

def is_even(n):
    return n % 2 == 0

c = lambda n: n % 2 == 0


def maximum(a, b):
    if a > b:
        return a
    return b

d = lambda a, b: a if a > b else b

def reverse_string(s):
    return s[::-1]

e = lambda e: e[::-1]


def sum_list(lst):
    total = 0
    for n in lst:
        total += n
    return total

f = lambda lst: sum(lst)
# print(sum_list([1, 2, 3, 4, 5]))
