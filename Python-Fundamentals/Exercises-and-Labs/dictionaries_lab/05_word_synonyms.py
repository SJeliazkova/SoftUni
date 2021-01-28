n = int(input())

synonyms = {}

for i in range(n):
    key_word = input()
    synonym = input()

    if key_word not in synonyms:
        synonyms[key_word] = []

    synonyms[key_word].append(synonym)

for key_word in synonyms:
    print(f"{key_word} - {', '.join(synonyms[key_word])}")
