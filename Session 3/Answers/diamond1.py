# Show factorial of even numbers from 1 to 20
for num in range(2, 21, 2):  # only even numbers
    fact = 1
    for i in range(1, num+1):  # calculate factorial
        fact *= i
    print(f"Factorial of {num} is {fact}")