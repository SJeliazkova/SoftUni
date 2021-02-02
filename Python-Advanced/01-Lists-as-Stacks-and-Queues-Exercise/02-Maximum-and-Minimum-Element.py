n = int(input())

nums = [ ]

for _ in range(n):
    data = input().split(" ")
    command = int(data[ 0 ])

    if command == 1:
        nums.append(int(data[ 1 ]))

    elif command == 2:
        if nums:
            nums.pop()
    elif command == 3:
        if nums:
            print(max(nums))
    elif command == 4:
        if nums:
            print(min(nums))

print(", ".join([str(x) for x in reversed(nums)]))
