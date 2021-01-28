happiness = list(map(int, input(). split()))
factor = int(input())

improve_happiness = list(map(lambda x: x * factor, happiness))

average_happiness = sum(improve_happiness) / len(improve_happiness)

filtered = list(filter(lambda x: x >= average_happiness, improve_happiness))

if len(filtered) >= len(happiness) / 2:
    print(f"Score: {len(filtered)}/{len(happiness)}. Employees are happy!")

else:
    print(f"Score: {len(filtered)}/{len(happiness)}. Employees are not happy!")