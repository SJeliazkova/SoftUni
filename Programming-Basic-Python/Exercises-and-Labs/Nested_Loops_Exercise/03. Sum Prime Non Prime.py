command = input()

sum_prime = 0
sum_no_prime = 0

while command != "stop":
    number = int(command)

    if number < 0:
        print("Number is negative.")

    else:
        counter = 0

        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1

        if counter == 2:
            sum_prime += number
        elif counter > 2:
            sum_no_prime += number

    command = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_no_prime}')

