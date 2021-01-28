line = input()
for i in range(len(line)):
    if line[i] == ":":
        print(line[i:i + 2])