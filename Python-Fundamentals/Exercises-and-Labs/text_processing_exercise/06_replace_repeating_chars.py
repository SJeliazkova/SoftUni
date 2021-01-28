text = input()

new_text = ""
new_letter = ""

for letter in text:
    if not letter == new_letter:
        new_text += letter
    new_letter = letter

print(new_text)