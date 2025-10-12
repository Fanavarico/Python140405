odd_even_dict = {
    "odd": [n for n in range(101, 201) if n % 2 != 0],
    "even": [n for n in range(101, 201) if n % 2 == 0]
}

print(odd_even_dict)