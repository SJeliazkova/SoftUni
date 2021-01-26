needed_nylon = int(input())
needed_paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = (needed_nylon + 2) * 1.5
paint_price = needed_paint * 1.1 * 14.50
thinner_price = thinner * 5

total_price_materials = nylon_price + paint_price + thinner_price + 0.4

workers_price = total_price_materials * 0.30 * hours

total_price_repainting = total_price_materials + workers_price

print(f"Total expenses: {total_price_repainting:.2f} lv.")