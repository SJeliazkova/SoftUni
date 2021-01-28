text = input()

final_text = ""
strength = 0

for index in range(len(text)):
    char_in_text = text[index ]

    if char_in_text == ">":
        strength += int(text[ index + 1 ])
        final_text += char_in_text
    elif not strength == 0:
        strength -= 1
    else:
        final_text += char_in_text

print(final_text)
