n = int(input())
counter = 0
balance = 0

while counter < n:
    money = float(input())

    if money < 0:
        print(f"Invalid operation!")
        break

    balance += money
    print(f"Increase: {money:.2f}")

    counter += 1

print(f"Total: {balance:.2f}")