import deck

main = deck.Deck(deck_count=2, debug=False)

# EXAMPLE HAND
example_hand = [
        deck.Deck.Card(suite="diamonds", rank="king"),
        deck.Deck.Card(suite="spades", rank="king"),
        deck.Deck.Card(suite="spades", rank="ace")
]


def total(hand):  # Aces have to be last  TODO: auto sorting of aces
    total = 0
    total_type = "hard"
    for card in hand:
        if card.rank in ["jack", "queen", "king"]:
            total += 10
        elif card.rank == "ace":
            if total >= 11:
                total_type = "soft"
                total += 1
            else:
                total += 11
        else:
            total += card.value
    return total, total_type


print(total(example_hand))
