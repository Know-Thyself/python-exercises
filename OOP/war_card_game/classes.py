import random
from global_vars import suits, ranks, values


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

    def get_card(self):
        return {"suit": self.suit, "rank": self.rank, "value": self.value}


class Deck:
    def __init__(self):
        self.all_cards = []
        for rank in ranks:
            for suit in suits:
                card = Card(suit, rank)
                self.all_cards.append(card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

    def get_all_cards(self):
        cards = []
        for card in self.all_cards:
            cards.append(card.get_card())
        return cards


class Player:
    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.cards = []

    def remove_one(self):
        # We state 0 to remove from the "top" of the deck
        return self.cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            for card in new_cards:
                self.cards.append(card)
        else:
            self.cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.cards)} cards."
