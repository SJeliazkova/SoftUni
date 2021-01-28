data = input().split()

products = {}

for index in range(0, len(data), 2):
    food = data[index]
    value = int(data[index + 1])

    products[food] = value

data_2 = input().split()

for el in data_2:
    if el in products:
        print(f"We have {products[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")


