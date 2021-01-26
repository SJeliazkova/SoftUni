num_1 = int(input())
num_2 = int(input())

for current_num in range( num_1, num_2 + 1):
    num_as_str = str(current_num)
    sum_even = 0
    sum_odd = 0
    for i in range(0, len(num_as_str)):
        digit = int(num_as_str[i])

        if (i + 1) % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

    if sum_even == sum_odd:
        print(current_num, end=" ")

