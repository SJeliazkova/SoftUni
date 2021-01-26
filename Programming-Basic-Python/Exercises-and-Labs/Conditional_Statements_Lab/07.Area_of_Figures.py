import math
figures = input()
area = 0
if figures == "square":
    side = float(input())
    area = side * side
elif figures == "rectangle":
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
elif figures == "circle":
    r = float(input())
    area = math.pi * r * r
elif figures == "triangle":
    side = float(input())
    height = float(input())
    area = side * height / 2

print(f"{area:.3f}")