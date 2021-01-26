men = int(input())
women = int(input())
max_tables = int(input())

table_counter = 0

for m in range(1, men + 1):
    for w in range(1, women + 1):

        if table_counter == max_tables:
            break
        else:
            print(f"({m} <-> {w})", end=" ")
            table_counter += 1

    if table_counter == max_tables:
        break


