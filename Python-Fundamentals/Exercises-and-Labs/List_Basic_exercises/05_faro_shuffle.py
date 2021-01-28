cards = input().split()
shuffles = int(input())

top_card = cards[0]
bottom_card = cards[-1]

half = len(cards) // 2

for shuffle in range(shuffles):

    shuffle_cards = []

    for index in range(half):
        first_card = cards[ index ]

        second_index = index + half
        second_card = cards[ second_index ]

        shuffle_cards.append(first_card)
        shuffle_cards.append(second_card)

    cards = shuffle_cards

print(shuffle_cards)
