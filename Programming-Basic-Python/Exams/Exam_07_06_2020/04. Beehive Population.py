import math

population = int(input())
years = int(input())

for i in range(1, years + 1):
    new_bees = math.floor(population / 10) * 2
    population += new_bees

    if i % 5 == 0 or i % 5 == 5:
        leaving_bees = math.floor(population / 50) * 5
        population -= leaving_bees

    dead_bees = math.floor(population / 20) * 2
    population -= dead_bees

print(f"Beehive population: {population}")
