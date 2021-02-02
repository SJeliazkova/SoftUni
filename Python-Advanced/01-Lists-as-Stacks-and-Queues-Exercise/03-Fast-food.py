from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])
order_completed = True

print(max(orders))

while orders:
    current_order = orders.popleft()

    if food_quantity >= current_order:
        food_quantity -= current_order

    else:
        order_completed = False
        orders.appendleft(current_order)
        break

if order_completed:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")

