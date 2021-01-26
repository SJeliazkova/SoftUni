championship_part = input()
ticket_type = input()
ticket_count = int(input())
picture = input()

ticket_price = 0
discount_photo = False

if championship_part == "Quarter final" and ticket_type == "Standard":
    ticket_price = 55.50
elif championship_part == "Quarter final" and ticket_type == "Premium":
    ticket_price = 105.20
elif championship_part == "Quarter final" and ticket_type == "VIP":
    ticket_price = 118.90

elif championship_part == "Semi final" and ticket_type == "Standard":
    ticket_price = 75.88
elif championship_part == "Semi final" and ticket_type == "Premium":
    ticket_price = 125.22
elif championship_part == "Semi final" and ticket_type == "VIP":
    ticket_price = 300.40

elif championship_part == "Final" and ticket_type == "Standard":
    ticket_price = 110.10
elif championship_part == "Final" and ticket_type == "Premium":
    ticket_price = 160.66
elif championship_part == "Final" and ticket_type == "VIP":
    ticket_price = 400

sum_tickets = ticket_price * ticket_count

if 2500 < sum_tickets <= 4000:
    sum_tickets = sum_tickets * 0.90

elif sum_tickets > 4000:
    sum_tickets = sum_tickets * 0.75
    discount_photo = True

if picture == 'Y':
    picture_sum = ticket_count * 40
    sum_tickets += picture_sum
    if discount_photo:
        sum_tickets -= picture_sum
elif picture == 'N':
    sum_tickets = sum_tickets

print(f"{sum_tickets:.2f}")
