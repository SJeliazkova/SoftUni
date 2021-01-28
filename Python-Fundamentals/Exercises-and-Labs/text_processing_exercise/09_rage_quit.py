line = input()

current_result = ""
final_result = ""
index = 0

while index < len(line):
    if not line[index].isdigit():
        current_result += line[index]
        index += 1
    else:
        number = ""
        while index < len(line) and line[index].isdigit():
            number += line[index]
            index += 1

        number = int(number)
        current_result = current_result.upper() * number
        final_result += current_result
        current_result = ""

print(f"Unique symbols used: {len(set(final_result))}")
print(final_result)


