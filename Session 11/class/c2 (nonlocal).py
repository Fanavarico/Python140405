# Click counter - count in outer - increase with inner
# Call outer from outside

# function
def click():
    total_click = 0

    def increase_click():
        nonlocal total_click
        total_click += 1

    increase_click()
    print(total_click)
    increase_click()
    print(total_click)
# function

# main
click()
# main



