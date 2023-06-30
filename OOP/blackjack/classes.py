import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def get_card(self):
        return {"suit": self.suit, "rank": self.rank}


class Deck:
    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                card = Card(suit, rank)
                self.deck.append(card)

    def get_all_cards(self):
        cards = []
        for card in self.deck:
            cards.append(card.get_card())
        return cards

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        cards = []
        for _ in range(2):
            cards.append(self.deck.pop())
        return cards

    def hit(self):
        return self.deck.pop(0)

    def reset(self):
        self.__init__()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value = values[card.rank]
        for card in self.cards:
            if card.rank == 'Ace':
                self.aces += 1

    def get_value(self):
        return self.value

    def adjust_for_ace(self):
        sum_total = 0
        for card in self.cards:
            sum_total += card.value
        for card in self.cards:
            if sum_total > 21 and card.rank == 'Ace':
                card.value = 1

    def reset(self):
        self.__init__()


class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def place_bet(self, bet):
        self.bet += bet

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
