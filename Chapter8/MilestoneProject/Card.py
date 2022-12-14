from collections import OrderedDict


class Card:
    VALUES_OF_RANKS = {'ace': 11, 'ten': 10, 'nine': 9, 'eight': 8,
                       'seven': 7, 'six': 6, 'five': 5, 'four': 4,
                       'three': 3, 'two': 2, 'king': 10, 'queen': 10,
                       'jack': 10}

    SUITS = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
    RANKS = VALUES_OF_RANKS.keys()

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.VALUES_OF_RANKS[rank]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit + " " + str(self.value)
