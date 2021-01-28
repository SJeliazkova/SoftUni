import re

line = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+)+"

emails = re.finditer(pattern, line)
for el in emails:
    print(el.group())