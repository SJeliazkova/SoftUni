budget = float(input())
flour_price = float(input())
one_pack_eggs_price = 0.75 * flour_price
milk_price_per_l = 1.25 * flour_price

cozonac_price = one_pack_eggs_price + flour_price + milk_price_per_l * 0.25
cozonac_count = 0
colored_eggs = 0


while budget >= cozonac_price:
    cozonac_count += 1
    budget -= cozonac_price
    colored_eggs += 3

    if cozonac_count % 3 == 0:
        colored_eggs -= (cozonac_count - 2)

print(f"You made {cozonac_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

