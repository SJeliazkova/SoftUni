import sys
import  math
easter_bread = int(input())

sugar = 0
flour = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize

for i in range( 1, easter_bread + 1):
    sugar_quantity = int(input())
    flour_quantity = int(input())

    sugar += sugar_quantity
    flour += flour_quantity

    if sugar_quantity > max_sugar:
        max_sugar = sugar_quantity
    if flour_quantity > max_flour:
        max_flour = flour_quantity

sugar_pack = math.ceil(sugar / 950)
flour_pack = math.ceil(flour / 750)

print(f"Sugar: {sugar_pack}")
print(f"Flour: {flour_pack}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")