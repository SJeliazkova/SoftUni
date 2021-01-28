messages = []

data = input()

while not data == "end":
    command = data.split()[0]
    message = data.split()[1]

    if command == "Chat":
        messages.append(message)

    elif command == "Delete":
        if message in messages:
            messages.remove(message)

    elif command == "Edit":
        message_to_edit = data.split()[1]
        edited_version = data.split()[2]

        index_m = messages.index(message_to_edit)
        messages[index_m] = edited_version

    elif command == "Pin":
        if message in messages:
            messages.remove(message)
            messages.append(message)

    elif command == "Spam":
        spam_message = data.split()[1:]

        for el in spam_message:
            messages.append(el)

    data = input()

print(*messages, sep= "\n")