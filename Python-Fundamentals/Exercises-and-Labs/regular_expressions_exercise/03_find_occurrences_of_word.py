import re

line = input().lower()
s_word = input().lower()

pattern = fr"\b{s_word}\b"

matches = re.findall(pattern, line)

print(len(matches))