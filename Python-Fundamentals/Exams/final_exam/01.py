text = input()

data = input()

while not data == "End":
    data = data.split()
    command = data[0]

    if command == "Translate":
        to_replace = data[1]
        replacement = data[2]
        text = text.replace(to_replace, replacement)
        print(text)

    elif command == "Includes":
        inc_string = data[1]
        if inc_string in text:
            print(True)
        else:
            print(False)

    elif command == "Start":
        start_str = data[1]
        text_as_list = text.split()
        if start_str == text_as_list[0]:
            print(True)
        else:
            print(False)

    elif command == "Lowercase":
        text = text.lower()
        print(text)

    elif command == "FindIndex":
        search_char = data[1]
        for i in range(len(text)-1, 0, -1):
            current_char = text[i]
            if current_char == search_char:
                print(i)
                break

    elif command == "Remove":
        start_index = int(data[1])
        count = int(data[2])
        part_to_remove = ""

        for i in range(start_index, start_index + count):
            part_to_remove += text[i]

        text = text.replace(part_to_remove, "")
        print(text)

    data = input()
