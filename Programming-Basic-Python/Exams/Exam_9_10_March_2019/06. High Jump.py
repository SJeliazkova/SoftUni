desired_height = int(input())

lath_height = desired_height - 30
jump_counter = 0

while lath_height <= desired_height:
    fail_counter = 0
    for h in range(1, 4):
        jump_height = int(input())
        jump_counter += 1

        if jump_height > lath_height:
            lath_height += 5
            break

        else:
            fail_counter += 1

    if fail_counter == 3:
        print(f"Tihomir failed at {lath_height}cm after {jump_counter} jumps.")
        break

if jump_height > desired_height:
    print(f"Tihomir succeeded, he jumped over {desired_height}cm after {jump_counter} jumps.")

