collecting_items = input().split(", ")

data = input()


def in_collection(element):
    if element not in collecting_items:
        res = False
    else:
        res = True
    return res


while not data == "Craft!":
    command, item = data.split(" - ")

    if command == "Collect":
        if not in_collection(item):
            collecting_items.append(item)

    elif command == "Drop":
        if in_collection(item):
            collecting_items.remove(item)

    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if in_collection(old_item):
            new_index = collecting_items.index(old_item) + 1
            collecting_items.insert(new_index, new_item)

    elif command == "Renew":
        if in_collection(item):
            collecting_items.remove(item)
            collecting_items.append(item)

    data = input()

print(", ".join(collecting_items))