eggs = int(input())

sold_eggs = 0

command = input()

while command != "Close":
    quantity = int(input())
    if command == "Buy":
        if quantity <= eggs:
            sold_eggs += quantity
            eggs -= quantity
        else:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs}.")
            break

    elif command == "Fill":
        eggs += quantity

    command = input()

else:
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")