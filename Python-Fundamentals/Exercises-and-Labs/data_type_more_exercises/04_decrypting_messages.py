key = int(input())
lines = int(input())

message = ""

for l in range(lines):
    character = input()
    new_character = chr(ord(character) + key)
    message += new_character

print(message)

