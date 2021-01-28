n = int(input())

left_space = 255
water_in_tank = 0

for i in range(1, n + 1):
    liters_of_water = int(input())
    if left_space < liters_of_water:
        print("Insufficient capacity!")
    else:
        left_space -= liters_of_water
        water_in_tank += liters_of_water

print(f"{water_in_tank}")