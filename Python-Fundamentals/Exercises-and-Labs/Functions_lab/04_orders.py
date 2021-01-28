def calc_price(item, quantity):
    result = 0
    if item == "coffee":
        result = quantity * 1.5
    elif item == "water":
        result = quantity * 1
    elif item == "coke":
        result = quantity * 1.4
    elif item == "snacks":
        result = quantity * 2

    return result

item = input()
quantity = float(input())
print(f"{calc_price(item, quantity):.2f}")
