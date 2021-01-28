def valid_password(password):
    is_valid = True
    if not (6 <= len(password) <= 10):
        is_valid = False
        print("Password must be between 6 and 10 characters")

    for symbol in password:
        if not symbol.isdigit() and not symbol.isalpha():
            is_valid = False
            print("Password must consist only of letters and digits")
            break

    digits_count = 0
    for symbol in password:
        if symbol.isdigit():
            digits_count += 1
    if digits_count < 2:
        is_valid = False
        print("Password must have at least 2 digits")


    return is_valid


checked_password = input()
is_valid = valid_password(checked_password)

if is_valid:
    print("Password is valid")