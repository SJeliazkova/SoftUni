shopping_list = input().split("!")
data = input()


def is_existing(s_list, item):
    if item in s_list:
        return True
    return False


while data != "Go Shopping!":
    data = data.split()
    command = data[0]
    product = data[1]

    if command == "Urgent":
        if not is_existing(shopping_list, product):
            shopping_list.insert(0, product)

    elif command == "Unnecessary":
        if is_existing(shopping_list, product):
            shopping_list.remove(product)

    elif command == "Correct":
        new_product = data[ 2 ]
        if is_existing(shopping_list, product):
            item_index = shopping_list.index(product)
            shopping_list.remove(product)
            shopping_list.insert(item_index, new_product)

    elif command == "Rearrange":
        if is_existing(shopping_list, product):
            shopping_list.remove(product)
            shopping_list.append(product)

    data = input()

print(', '.join(shopping_list))
