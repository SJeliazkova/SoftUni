width = int(input())
lenght = int(input())

cake_pieces = width * lenght

while cake_pieces > 0:
    command = input()

    if command == "STOP":
        print(f"{cake_pieces} pieces are left.")
        break
    else:
        taken_pieces = int(command)
        cake_pieces -= taken_pieces

else:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
