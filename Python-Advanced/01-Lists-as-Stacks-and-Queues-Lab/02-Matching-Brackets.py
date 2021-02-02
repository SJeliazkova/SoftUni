data = input()

s = []

for i in range(len(data)):
    current_char = data[i]

    if current_char == '(':
        s.append(i)
    elif current_char == ')':
        j = s.pop()
        print(data[j:i + 1])
