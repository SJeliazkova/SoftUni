n_electrons = int(input())

electrons = []
index_cell = 1

while n_electrons > 0:
    possible_electrons = 2 * index_cell ** 2

    if possible_electrons > n_electrons:
        electrons.append(n_electrons)
    else:
        electrons.append(possible_electrons)

    n_electrons -= possible_electrons
    index_cell += 1

print(electrons)




