bees_count = int(input())
flowers_count = int(input())

total_honey = bees_count * flowers_count * 0.21
honeycombs = total_honey // 100
left_honey = total_honey - honeycombs * 100

print(f"{honeycombs:.0f} honeycombs filled.")
print(f"{left_honey:.2f} grams of honey left.")
