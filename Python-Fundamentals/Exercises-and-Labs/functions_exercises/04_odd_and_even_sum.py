def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for i in range(0, len(number)):
        current_digit = int(number[i])
        if current_digit % 2 == 0:
            even_sum += current_digit
        else:
            odd_sum += current_digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

num = input()
print(odd_even_sum(num))