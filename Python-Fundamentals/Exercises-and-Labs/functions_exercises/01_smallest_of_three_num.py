def smallest_num(num_1, num_2, num_3):
    numbers = [num_1, num_2, num_3]
    numbers.sort()
    return numbers[0]

n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
print(smallest_num(n_1, n_2, n_3))