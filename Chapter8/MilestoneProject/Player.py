class Player:

    def __init__(self, name):
        self.name = name
        self.deck_of_cards = []

    def add_cards(self, cards):
        if isinstance(cards, type([])):
            self.deck_of_cards.extend(cards)
        else:
            self.deck_of_cards.append(cards)

    def remove_cards(self):
        self.deck_of_cards = []

    def __str__(self):
        return f'player {self.name} has {len(self.deck_of_cards)} cards\n'

    def wipe_cards(self):
        self.deck_of_cards = []

