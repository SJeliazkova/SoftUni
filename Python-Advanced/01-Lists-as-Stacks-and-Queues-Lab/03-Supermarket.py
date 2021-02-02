from _collections import deque

END_COMMAND = "End"
PAID_COMMAND = "Paid"

name_queue = deque()

while True:
    command = input()
    if command == END_COMMAND:
        print(f"{len(name_queue)} people remaining.")
        break
    elif command == PAID_COMMAND:
        while name_queue:
            print(name_queue.popleft())
    else:
        name_queue.append(command)