text = input()

symbols = {}

for ch in text:
    symbols[ch] = text.count(ch)

for k, v in sorted(symbols.items()):
    print(f"{k}: {v} time/s")