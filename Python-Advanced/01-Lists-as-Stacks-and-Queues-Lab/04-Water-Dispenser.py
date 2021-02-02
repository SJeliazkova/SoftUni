from _collections import deque

START_COMMAND = 'Start'
END_COMMAND = "End"
REFILL_COMMAND = "refill"

water_quantity = int(input())

peoples_queue = deque()

while True:
    command = input()

    if command == START_COMMAND:
        break
    peoples_queue.append(command)

while True:
    command = input()
    if command == END_COMMAND:
        print(f"{water_quantity} liters left")
        break

    if command.startswith(REFILL_COMMAND):
        command_info = command.split(' ')
        refill_liters = int(command_info[1])
        water_quantity += refill_liters
    else:
        person = peoples_queue.popleft()
        person_liters = int(command)

        if person_liters <= water_quantity:
            print(f"{person} got water")
            water_quantity -= person_liters
        else:
            print(f"{person} must wait")

