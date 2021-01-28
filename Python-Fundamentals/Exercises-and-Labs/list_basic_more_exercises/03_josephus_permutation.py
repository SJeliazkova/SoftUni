data = input().split()
step = int(input())

new_list = []

index = 0

while len(data) > 0:
    index = (index + step - 1) % len(data)
    new_list.append(data[index])
    data.remove(data[index])

print(f"[{','.join(new_list)}]")
