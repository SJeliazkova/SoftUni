def sum_numbers(num_1, num_2):
    sum_result = num_1 + num_2
    return sum_result


def subtract(num_3) -> object:
    subtract_result = - num_3
    return subtract_result


def add_and_subtract(num_1, num_2, num_3):
    result = sum_numbers(num_1, num_2) + subtract(num_3)
    return result


n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

print(add_and_subtract(n_1, n_2, n_3))
