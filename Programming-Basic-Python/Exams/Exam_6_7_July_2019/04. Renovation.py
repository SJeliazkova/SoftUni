import math
height_wall = int(input())
width_wall = int(input())
percent_holes = int(input())

walls_area = height_wall * width_wall * 4
paining_area = math.ceil(walls_area - walls_area * percent_holes / 100)

command = input()
while command != "Tired!":
    paint_quantity = int(command)
    paining_area -= paint_quantity

    if paining_area > 0:
        command = input()

    else:
        left_paint = abs(paining_area)
        if left_paint != 0:
            print(f"All walls are painted and you have {left_paint} l paint left!")

        elif left_paint == 0:
            print("All walls are painted! Great job, Pesho!")
        break

else:
    print(f"{paining_area} quadratic m left.")








