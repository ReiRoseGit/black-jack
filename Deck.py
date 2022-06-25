import const
from itertools import product
from random import shuffle


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.suit} {self.rank}, value: {self.value}"


class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        shuffle(self.cards)

    def create_deck(self):
        deck = []
        for rank, suit in product(const.RANKS, const.SUITS):
            if rank == 'ace':
                deck.append(Card(rank, suit, 11))
            elif rank == 'jack':
                deck.append(Card(rank, suit, 2))
            elif rank == 'queen':
                deck.append(Card(rank, suit, 3))
            elif rank == 'king':
                deck.append(Card(rank, suit, 4))
            else:
                deck.append(Card(rank, suit, int(rank)))
        return deck

    def __len__(self):
        return len(self.cards)

    def take_card(self):
        return self.cards.pop()

    def start_hand(self):
        return [self.take_card(), self.take_card()]

    def __str__(self):
        s = ""
        for c in self.cards:
            s += c.__str__ + " "
        return s
