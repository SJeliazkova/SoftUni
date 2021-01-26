movie_name = input()

student_counter = 0
standard_counter = 0
kid_counter = 0

while movie_name != "Finish":
    free_seats = int(input())
    ticket_type = input()

    ticket_counter = 0

    while ticket_type != "End":
        ticket_counter += 1

        if ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        elif ticket_type == "kid":
            kid_counter += 1

        if ticket_counter == free_seats:
            break

        ticket_type = input()

    percent_full = ticket_counter / free_seats * 100

    print(f"{movie_name} - {percent_full:.2f}% full.")

    movie_name = input()

total_tickets = kid_counter + student_counter + standard_counter
standard_percent = standard_counter / total_tickets * 100
student_percent = student_counter / total_tickets * 100
kid_percent = kid_counter / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")







