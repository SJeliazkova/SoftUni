flour_price = float(input())
flour_quantity = float(input())
sugar_quantity = float(input())
eggs_quantity = int(input())
baking_yeast_quantity = int(input())

sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.1
baking_yeast_price = 0.2 * sugar_price

total_sum = flour_price * flour_quantity + sugar_price * sugar_quantity + \
            eggs_price * eggs_quantity + baking_yeast_price * baking_yeast_quantity

print(f"{total_sum:.2f}")