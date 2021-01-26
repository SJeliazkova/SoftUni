n = int(input())

for num in range(1111, 10000):
    digit_1 = num // 1000
    digit_2 = (num // 100) % 10
    digit_3 = (num // 10) % 10
    digit_4 = num % 10

    check_1 = digit_1 != 0 and n % digit_1 == 0
    check_2 = digit_2 != 0 and n % digit_2 == 0
    check_3 = digit_3 != 0 and n % digit_3 == 0
    check_4 = digit_4 != 0 and n % digit_4 == 0

    if check_1 and check_2 and check_3 and check_4:
        print(f"{num}", end=" ")