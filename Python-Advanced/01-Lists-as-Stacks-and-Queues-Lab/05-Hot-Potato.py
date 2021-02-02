from _collections import deque

name_queue = input().split(" ")
step = int(input())

q = deque(name_queue)
counter = 0

while len(q) > 1:
    for i in range(step - 1):
        q.append(q.popleft())
    print(f"Removed {q.popleft()}")


print(f"Last is {q.popleft()}")

