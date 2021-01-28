version = input().split(".")
version_as_num = ''.join(version)

next_version_num = int(version_as_num) + 1
next_version_str = str(next_version_num)

print(".".join(next_version_str))



