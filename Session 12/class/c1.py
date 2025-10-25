# function -> calculate_footbal_score

# function - local
def calculate_footbal_score(score):
    global total_scores

    total_scores += score

# global
total_scores = 0
calculate_footbal_score(10)
calculate_footbal_score(10)
print(total_scores)



# type hinting
# name, last_name, age -> [name, last_name, age]
def show_student_detail(name: str, last_name: str, age: str) -> list[str]:
    """
    this function returns a list of student data
    """
    return [name, last_name, age]


# nemidoni chanta kala toye sabade kahride
def average_shop_cart_items(*args):
    print(sum(args) / len(args))

average_shop_cart_items(10, 20, 100, 200)