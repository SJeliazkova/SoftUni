voucher_value = int(input())

ticket_price = 0
other_price = 0
tickets = 0
others = 0

while voucher_value > 0:
    command = input()
    if command == "End":
        break

    else:
        lenght_name = len(command)
        if lenght_name > 8: # билет за кино

            first_symbol = command[0]
            second_symbol = command[1]
            ticket_price = ord(first_symbol) + ord(second_symbol)
            if ticket_price <= voucher_value:
                tickets += 1
                voucher_value -= ticket_price
            else:
                break

        else: # покупка

            first_symbol = command[0]
            other_price = ord(first_symbol)

            if other_price <= voucher_value:
                others += 1
                voucher_value -= other_price
            else:
                break

print(tickets)
print(others)

