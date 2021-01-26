first_digit = int(input())
second_digit = int(input())
third_digit = int(input())

for i in range(1, first_digit + 1):
    if i % 2 == 0:
        symbol_1 = i

        for j in range(1, second_digit + 1):
            if j == 2 or j == 3 or j == 5 or j == 7:
                symbol_2 = j

                for k in range(1, third_digit + 1):
                    if k % 2 == 0:
                        symbol_3 = k

                        print(f"{symbol_1} {symbol_2} {symbol_3}")