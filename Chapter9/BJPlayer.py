from Chapter8.MilestoneProject.Player import Player
from Chapter9.BJCard import BJCard


class BJPlayer(Player):
    def __init__(self, name, player_type):
        super().__init__(name)
        self.player_type = player_type

    def __str__(self):
        return f'{self.player_type} {self.name}'

    def print_deck(self):
        return [str(x) for x in self.deck_of_cards]

