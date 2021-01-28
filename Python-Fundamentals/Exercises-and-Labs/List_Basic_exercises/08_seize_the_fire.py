
RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)

fire = input().split("#")
water = int(input())

effort = 0
put_out_fire = []

for n_fire in fire:
    fire_cell = n_fire.split(" = ")
    fire_type = fire_cell[0]
    fire_value = int(fire_cell[1])

    if fire_type == "High" and fire_value not in RANGE_HIGH:
        continue
    elif fire_type == "Medium" and fire_value not in RANGE_MEDIUM:
        continue
    elif fire_type == "Low" and fire_value not in RANGE_LOW:
        continue

    if water >= fire_value:
        water -= fire_value
        effort += fire_value * 0.25
        put_out_fire.append(fire_value)

print("Cells:")
for fire_value in put_out_fire:
    print(f" - {fire_value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_fire)}")



