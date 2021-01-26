customers = int(input())

total_price = 0

for i in range(1, customers + 1):
    product = input()
    products_price = 0
    product_sum = 0

    while product != "Finish":

        if product == "basket":
            products_price += 1.50
            product_sum += 1
        elif product == "wreath":
            products_price += 3.80
            product_sum += 1
        elif product == "chocolate bunny":
            products_price += 7
            product_sum += 1

        product = input()

    else:
        if product_sum % 2 == 0:
            products_price = products_price * 0.80

        total_price += products_price
        print(f"You purchased {product_sum} items for {products_price:.2f} leva.")

average = total_price / customers
print(f"Average bill per client is: {average:.2f} leva.")


