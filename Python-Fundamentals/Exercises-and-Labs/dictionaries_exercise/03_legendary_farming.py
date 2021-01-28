mapper = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

materials = {"shards": 0, "fragments": 0, "motes": 0}
junks = {}

while True:
    data = input().split()
    is_found = False
    for i in range(0, len(data), 2):
        value = int(data[i])
        item = data[i + 1].lower()

        if item in materials:
            materials[item] += value
        else:
            if item not in junks:
                junks[item] = value
            else:
                junks[item] += value

        for key, value in materials.items():
            if value >= 250:
                print(f"{mapper[key]} obtained!")
                materials[key] -= 250
                is_found = True
                break

        if is_found:
            break

    if is_found:
        break

ordered_materials = sorted(materials.items(), key=lambda x: (-x[1], x[0]))

for item, value in ordered_materials:
    print(f'{item}: {value}')

ordered_junks = sorted(junks.items(), key=lambda x: x[0])

for junk, junk_value in ordered_junks:
    print(f'{junk}: {junk_value}')



