data = input().split()

words = {}

for el in data:
    el = el.lower()
    if el not in words:
        words[el] = 0
    words[el] += 1

for key, value in words.items():
    if value % 2 != 0:
        print(key, end=" ")

