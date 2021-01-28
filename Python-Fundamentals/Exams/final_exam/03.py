data = input()

followers = {}

while not data == "Log out":
    data = data.split(": ")
    command = data[0]
    name = data[1]

    if command == "New follower":
        if name not in followers:
            followers[name] = 0

    elif command == "Like":
        count = int(data[2])
        if name not in followers:
            followers[name] = count
        else:
            followers[name] += count

    elif command == "Comment":
        if name not in followers:
            followers[name] = 1
        else:
            followers[name] += 1

    elif command == "Blocked":
        key_to_remove = name
        if key_to_remove not in followers:
            print(f"{name} doesn't exist.")
        else:
            del followers[key_to_remove]

    data = input()

sorted_followers = sorted(followers.items(), key=lambda x: (-x[1], x[0]))

print(f"{len(followers)} followers")
for key, value in sorted_followers:
    print(f'{key}: {value}')


