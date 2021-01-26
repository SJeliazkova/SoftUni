flower_type = input()
flower_count = int(input())
season = input()

honey_per_flower = 0
total_honey = 0

if season == "Spring" and flower_type == "Sunflower":
    honey_per_flower = 10
elif season == "Spring" and flower_type == "Daisy":
    honey_per_flower = 12 * 1.1
elif season == "Spring" and flower_type == "Lavender":
    honey_per_flower = 12
elif season == "Spring" and flower_type == "Mint":
    honey_per_flower = 10 * 1.1

elif season == "Summer" and flower_type == "Sunflower":
    honey_per_flower = 8
elif season == "Summer" and flower_type == "Daisy":
    honey_per_flower = 8
elif season == "Summer" and flower_type == "Lavender":
    honey_per_flower = 8
elif season == "Summer" and flower_type == "Mint":
    honey_per_flower = 12

elif season == "Autumn" and flower_type == "Sunflower":
    honey_per_flower = 12
elif season == "Autumn" and flower_type == "Daisy":
    honey_per_flower = 6
elif season == "Autumn" and flower_type == "Lavender":
    honey_per_flower = 6
elif season == "Autumn" and flower_type == "Mint":
    honey_per_flower = 6

honey = honey_per_flower * flower_count

if season == "Summer":
    total_honey = honey * 1.1
elif season == "Autumn":
    total_honey = honey * 0.95
elif season == "Spring":
    total_honey = honey

print(f"Total honey harvested: {total_honey:.2f}")


