import math

a1 = int(input())
a2 = int(input())
n = int(input())

res = math.floor(n / 2)

for i in range(a1, a2):
    symbol_1 = chr(i)
    for j in range(1, n):
        symbol_2 = j
        for k in range(1, res):
            symbol_3 = k
            symbol_4 = ord(symbol_1)

            check_1 = symbol_4 % 2 != 0
            check_2 = (symbol_2 + symbol_3 + symbol_4) % 2 != 0

            if check_1 and check_2:

                print(f"{symbol_1}-{symbol_2}{symbol_3}{symbol_4}")