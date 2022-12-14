from random import shuffle

from Chapter9.BJCard import BJCard


class DeckOfCards:
    def __init__(self):
        self.deck_of_cards = None

    def create_deck_of_cards(self):
        deck = []
        for suit in BJCard.SUITS:
            for rank in BJCard.RANKS:
                deck.append(BJCard(suit, rank, False))
        self.deck_of_cards = deck
        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.deck_of_cards)

    def __str__(self):
        deck = ''
        for index, card in enumerate(self.deck_of_cards):
            deck += str(card).center(20) + ", "
        return deck[0:len(deck) - 2]

    def pick_card(self):
        return self.deck_of_cards.pop(0)

    def __len__(self):
        return len(self.deck_of_cards)
