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

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp + '\n' + card.__str__()
        return deck_comp

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
        return self.deck.pop()

    def reset(self):
        self.__init__()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        for card in self.cards:
            if card.rank == 'Ace':
                self.aces += 1

    def __str__(self):
        card_comp = ''
        for card in self.cards:
            card_comp += '\n' + card.__str__()
        return card_comp

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

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
