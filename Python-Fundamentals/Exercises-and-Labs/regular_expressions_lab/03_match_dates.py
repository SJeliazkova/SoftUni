import re

data = input()

pattern = r"\b(?P<day>\d{2})(?P<sep>[\./-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})"

datas = re.finditer(pattern, data)

for d in datas:
    print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")