start = int(input())
end = int(input())
magic_num = int(input())

flag = False
counter = 0

for x in range(start, end+1):
    for y in range(start, end+1):
        counter += 1

        result = x + y

        if result == magic_num:
            print(f"Combination N:{counter} ({x} + {y} = {magic_num})")
            flag = True
            break

    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic_num}")
