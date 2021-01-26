start = int(input())
end = int(input())

for i in range(start, end + 1):
    for j in range(start, end + 1):
        for k in range(start, end + 1):
            for l in range(start, end + 1):

                check1 = i % 2 == 0 and l % 2 != 0
                check2 = i % 2 != 0 and l % 2 == 0
                check3 = i > l
                check4 = (j + k) % 2 == 0

                if ( check1 or check2 ) and check3 and check4:

                    print(f"{i}{j}{k}{l}", end=" ")
