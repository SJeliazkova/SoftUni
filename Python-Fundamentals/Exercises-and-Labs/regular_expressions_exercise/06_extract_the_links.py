import re

line = input()

pattern = r"(^|(?<=\s))w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+($|(?=\s))"

while line:
    for el in re.finditer(pattern, line):
        print(el.group(0))

    line = input()


