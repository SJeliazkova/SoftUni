n = int(input())

for num in range(1, n + 1):
    sum_of_digest = 0
    num_as_str = str(num)
    for char in num_as_str:
        sum_of_digest += int(char)

    if sum_of_digest == 5 or sum_of_digest == 7 or sum_of_digest == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")