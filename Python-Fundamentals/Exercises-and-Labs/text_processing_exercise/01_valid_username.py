def length(name):
    if 3 <= len(user_name) <= 16:
        return True


def contains(name):
    allowed_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-")
    validation = set(name)
    if validation.issubset(allowed_chars):
        return True


user_names = input().split(", ")

valid_user_names = []

for user_name in user_names:
    if length(user_name) and contains(user_name):
        valid_user_names.append(user_name)


for name in valid_user_names:
    print(name)
