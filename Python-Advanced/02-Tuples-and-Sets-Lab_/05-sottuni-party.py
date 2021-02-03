def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def input_to_list_until_command(end_command):
    lines = []
    while True:
        command = input()
        if command == end_command:
            break
        lines.append(command)
    return lines


def is_vip_guest(guest):
    return guest[0].isdigit()


def separate_into_vip_and_regular(guests):
    vip_guests = []
    regular_guest = []
    for g in guests:
        if is_vip_guest(g):
            vip_guests.append(g)
        else:
            regular_guest.append(g)

    return (sorted(vip_guests), sorted(regular_guest))


def print_result(guests):
    print(len(guests))
    (vip_guests, regular_guest) = separate_into_vip_and_regular(guests)

    for g in vip_guests:
        print(g)

    for g in regular_guest:
        print(g)


n = int(input())
reservations = input_to_list(n)

guests_arrived = input_to_list_until_command("END")

guests_not_arrived = set(reservations).difference(guests_arrived)

print_result(guests_not_arrived)

