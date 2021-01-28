import re

line = input()
pattern = r"(^>{2})(?P<name>\w+)<{2}(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|\s)"
names = []
totall_price = 0

while not line == "Purchase":
    match = re.match(pattern, line)
    if match:
        obj = match.groupdict()
        names.append(obj["name"])
        totall_price += float(obj["price"]) * int(obj["quantity"])

    line = input()

print("Bought furniture:")
for name in names:
    print(name)
print(f"Total money spend: {totall_price:.2f}")