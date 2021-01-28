import re

n_inputs = int(input())

pattern = r"[U][$](?P<name>[A-Z][a-z]{2}([a-z]+)?)[U][$][P][@][$](?P<pass>[A-Za-z]{5}([A-Za-z]+)?[0-9]+)[P][@][$]"
count = 0

for _ in range(n_inputs):
    reg = input()
    if re.match(pattern, reg):
        valid_reg = re.match(pattern, reg)
        name = valid_reg.group(1)
        password = valid_reg.group(3)
        print("Registration was successful")
        print(f"Username: {name}, Password: {password}")
        count += 1

    else:
        print("Invalid username or password")

print(f"Successful registrations: {count}")




