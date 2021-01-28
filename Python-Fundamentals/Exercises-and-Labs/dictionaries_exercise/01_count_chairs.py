words = input().split()

characters = {}

for word in words:
    for i in range(len(word)):
        current_letter = word[ i ]
        if current_letter not in characters:
            characters[ current_letter ] = 0
        characters[ current_letter ] += 1

for key, value in characters.items():
    print(f'{key} -> {value}')
