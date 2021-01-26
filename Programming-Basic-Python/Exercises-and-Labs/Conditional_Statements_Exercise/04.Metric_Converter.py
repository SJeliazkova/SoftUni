number = float(input())
unit_entr = input()
unit_exit = input()

if unit_entr == "mm":
    number = number / 1000
elif unit_entr == "cm":
    number = number /100

if unit_exit == "mm":
    number = number * 1000
elif unit_exit == "cm":
    number = number * 100

print(f"{number:.3f}")