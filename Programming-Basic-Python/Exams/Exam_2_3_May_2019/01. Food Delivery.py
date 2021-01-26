chicken_menu = int(input())
fish_menu = int(input())
veg_menu = int(input())

menu_price = chicken_menu * 10.35 + fish_menu * 12.40 + veg_menu * 8.15
total_price = menu_price + menu_price * 0.20 + 2.50

print(f"Total: {total_price:.2f}")