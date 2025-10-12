with open("movies.txt", "w") as file:
    for i in range(1, 8):
        movie = input(f"Enter movie {i} name: ")
        times = input(f"How many times did you watch {movie}? ")
        file.write(f"{movie} - {times} times\n")

print("All data saved to movies.txt ✅")