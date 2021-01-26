easter_bread = int(input())
eggshells = int(input())
cookies = int(input())

eggs = eggshells * 12

total_price = easter_bread * 3.20 + cookies * 5.40 + eggshells * 4.35 + \
    eggs * 0.15

print(f"{total_price:.2f}")