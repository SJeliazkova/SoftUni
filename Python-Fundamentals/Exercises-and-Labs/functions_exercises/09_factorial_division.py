def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


number_1 = int(input())
number_2 = int(input())

result = factorial(number_1) / factorial(number_2)
print(f"{result:.2f}")