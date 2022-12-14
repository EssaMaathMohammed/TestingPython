from collections import OrderedDict

from Chapter8.MilestoneProject.Card import Card


class BJCard(Card):

    def __init__(self, suit, rank, hidden):
        super().__init__(suit, rank)
        self.hidden = hidden

    def __str__(self):
        if self.hidden:
            return 'Hidden'
        else:
            return self.rank + " of " + self.suit + " " + str(self.value)
