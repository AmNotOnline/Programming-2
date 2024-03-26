from util import Card

def group_by_suit(cards: list[Card]):
    return {card.suit: list(filter(lambda c: c.suit == card.suit, cards)) for card in cards}