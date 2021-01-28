lines = int(input())
open_bracket = 0
close_bracket = 0
double_open = 0
double_close = 0

for l in range(lines):
    symbol = input()
    if symbol == "(":
        open_bracket += 1
        double_open += 1
        double_close = 0
    elif symbol == ")":
        close_bracket += 1
        double_open = 0
        double_close += 1
    if double_open == 2 or double_close == 2:
        break
if open_bracket == close_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")