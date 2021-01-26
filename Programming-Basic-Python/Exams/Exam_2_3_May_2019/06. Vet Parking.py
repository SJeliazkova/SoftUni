days = int(input())
hours = int(input())

total_tax = 0

for d in range(1, days + 1):
    tax = 0
    for h in range(1, hours + 1):

        check_1 = d % 2 == 0 and h % 2 != 0
        check_2 = d % 2 != 0 and h % 2 == 0

        if check_1:
            tax += 2.50
        elif check_2:
            tax += 1.25
        else:
            tax += 1

    total_tax += tax
    print(f"Day: {d} - {tax:.2f} leva")

print(f"Total: {total_tax:.2f} leva")
