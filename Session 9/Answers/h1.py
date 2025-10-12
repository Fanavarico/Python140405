countries = []
populations = []

country = input("Enter country name (or 'stop' to end): ")
population = int(input("Enter population (negative to stop): "))

while population > 0:
    
    countries.append(country)
    populations.append(population)

    country = input("Enter country name (or 'stop' to end): ")
    population = int(input("Enter population (negative to stop): "))

avg_population = sum(populations) / len(populations)

print("\nCountries:", countries)
print("Average population:", avg_population)