
eggs = int(input())

red_eggs = 0
orange_egs = 0
blue_eggs = 0
green_eggs = 0

for i in range(1, eggs+1):
    color = input()
    if color == "red":
        red_eggs += 1
    elif color == "orange":
        orange_egs += 1
    elif color == "blue":
        blue_eggs += 1
    elif color == "green":
        green_eggs += 1

max_eggs_color = "red"
max_eggs = red_eggs

if orange_egs > max_eggs:
    max_eggs = orange_egs
    max_eggs_color = "orange"
if blue_eggs > max_eggs:
    max_eggs = blue_eggs
    max_eggs_color = "blue"
if green_eggs > max_eggs:
    max_eggs = green_eggs
    max_eggs_color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_egs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {max_eggs_color}")

