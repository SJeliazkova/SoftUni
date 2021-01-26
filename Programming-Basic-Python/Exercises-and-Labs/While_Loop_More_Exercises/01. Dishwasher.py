number_of_bottles = int(input())

clean_dishes = 0
clean_pots = 0
left_detergent = 750 * number_of_bottles
charging = 0

while left_detergent >= 0:
    command = input()

    if command == "End":
        print(f"Detergent was enough!")
        print(f"{clean_dishes} dishes and {clean_pots} pots were washed.")
        print(f"Leftover detergent {left_detergent} ml.")
        break

    else:
        charging += 1
        if charging % 3 == 0:
            wash_dish = int(command)
            clean_pots += wash_dish
            left_detergent -= 15 * wash_dish
        else:
            wash_dish = int(command)
            clean_dishes += wash_dish
            left_detergent -= 5 * wash_dish


else:
    print(f"Not enough detergent, {abs(left_detergent)} ml. more necessary!")




