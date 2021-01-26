text = input()
lenght = len(text)
sum = 0

for index in range(0, lenght):
    letter = text[index]
    if letter == "a":
        sum += 1
    elif letter == "e":
        sum += 2
    elif letter == "i":
        sum += 3
    elif letter == "o":
        sum += 4
    elif letter == "u":
        sum += 5

print(sum)