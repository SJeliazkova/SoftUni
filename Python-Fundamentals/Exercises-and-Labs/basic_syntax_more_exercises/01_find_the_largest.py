n = input()
n_list = []
for i in n:
    current_digits = int(i)
    n_list.append(current_digits)

n_list.sort(reverse=True)

print(*n_list, sep='')

