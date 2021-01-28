text = input()

indexes = []

for i in range(0, len(text)):
    current_letter = text[i]
    if 65 <= ord(current_letter) <= 90:
        indexes.append(i)

print(indexes)

