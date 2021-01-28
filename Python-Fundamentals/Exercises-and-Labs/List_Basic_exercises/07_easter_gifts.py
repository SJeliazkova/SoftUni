gifts = input().split()
message = input()

while message != "No Money":
    message_list = message.split()
    command = message_list[0]
    gift = message_list[1]

    if command == "OutOfStock":
        for index in range(len(gifts)):
            if gifts[index] == gift:
                gifts[index] = "None"

    elif command == "Required":
        index = int(message_list[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif command == "JustInCase":
        gifts[-1] = gift

    message = input()

while "None" in gifts:
    gifts.remove("None")

print(' '.join(gifts))
