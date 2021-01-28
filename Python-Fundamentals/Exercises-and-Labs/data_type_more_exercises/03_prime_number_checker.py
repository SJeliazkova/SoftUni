num = int(input())

divisor_counter = 0

for n in range(1, num + 1):
    if num % n == 0:
        divisor_counter += 1

if divisor_counter > 2:
    print(False)
else:
    print(True)
