def play_round(list_cards, i_1, i_2, round_num):
    if i_1 == i_2 or i_1 not in range(len(list_cards)) or i_2 == i_1 or i_2 not in range(len(list_cards)):
        print("Invalid input! Adding additional elements to the board")
        middle = len(list_cards) // 2
        list_cards.insert(middle, f"-{round_num}a")
        list_cards.insert(middle, f"-{round_num}a")
        return list_cards

    if list_cards[i_1] == list_cards[i_2]:
        element = list_cards[i_1]
        print(f"Congrats! You have found matching elements - {element}!")
        list_cards.remove(element)
        list_cards.remove(element)
        return list_cards
    print("Try again!")
    return list_cards


cards = [int(el) for el in input().split()]

indexes = input()
counter = 0

while not indexes == "end":
    index_1, index_2 = [int(i) for i in indexes.split()]
    counter += 1
    cards = play_round(cards, index_1, index_2, counter)

    if len(cards) == 0:
        print(f"You have won in {counter} turns!")
        exit(0)

    indexes = input()

print("Sorry you lose :(")
print(' '.join([str(el) for el in cards]))
