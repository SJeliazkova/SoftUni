n = int(input())

register = {}

for _ in range(n):
    data = input().split()
    command = data[0]
    name = data[1]

    if command == "register":
        reg_num = data[2]
        if name not in register:
            register[name] = reg_num
            print(f"{name} registered {reg_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {reg_num}")

    elif command == "unregister":
        if name not in register:
            print(f"ERROR: user {name} not found")
        else:
            register.pop(name)
            print(f"{name} unregistered successfully")

for name, reg_num in register.items():
    print(f"{name} => {reg_num}")
