end_sector = input()
rows = int(input())
odd_seats = int(input())

seas_counter = 0

for s in range(65, ord(end_sector) + 1):

    for r in range(1, rows + 1):

        if r % 2 != 0:
            for ss in range(97, odd_seats + 97):
                seas_counter += 1
                print(f"{chr(s)}{r}{chr(ss)}", end=" ")
                print()


        else:
            for ss in range(97, 97 + odd_seats + 2):
                seas_counter += 1
                print(f"{chr(s)}{r}{chr(ss)}", end=" ")
                print()

    rows += 1

print(seas_counter)