animals = input().split(", ")

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")

else:
    index = animals.index("wolf")
    print(f"Oi! Sheep number {len(animals) - index - 1}! You are about to be eaten by a wolf!")