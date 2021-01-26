
steps_counter = 0

while steps_counter < 10000:
    command = input()

    if command == "Going home":
        steps_to_home = int(input())
        steps_counter += steps_to_home
        break

    else:
        steps_counter += int(command)

if steps_counter >= 10000:
    print("Goal reached! Good job!")
else:
    left_steps = 10000 - steps_counter
    print(f"{left_steps} more steps to reach goal.")