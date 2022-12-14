from Chapter8.MilestoneProject.DeckOfCards import DeckOfCards
from Chapter8.MilestoneProject.Player import Player

my_dec = DeckOfCards()
player_one = Player('essa')
player_two = Player('nada')


def deal_cards():
    my_dec.create_deck_of_cards()
    for _ in range(int(len(my_dec) / 2)):
        player_one.add_cards(my_dec.pick_card())
        player_two.add_cards(my_dec.pick_card())


def start_war(player_one_table, player_two_table):
    winner = ''
    war_is_on = True
    while war_is_on:
        if len(player_one.deck_of_cards) == 0:
            winner = player_two
            return winner, player_one_table + player_two_table
        elif len(player_two.deck_of_cards) == 0:
            winner = player_one
            return winner, player_one_table + player_two_table

        player_one_table.append(player_one.remove_cards())
        player_two_table.append(player_two.remove_cards())

        print(f'Player 1 Picked {str(player_one_table[-1])}')
        print(f'Player 2 Picked {str(player_two_table[-1])}')

        if player_one_table[-1].value > player_two_table[-1].value:
            winner = player_one
            war_is_on = False
        elif player_one_table[-1].value < player_two_table[-1].value:
            winner = player_two
            war_is_on = False
    print('------- War ended -------')
    return winner, player_one_table + player_two_table


def evaluate():
    player_one_table = [player_one.remove_cards()]
    player_two_table = [player_two.remove_cards()]

    print(f'Player 1 Hand {str(player_one_table[0])}')
    print(f'Player 2 Hand {str(player_two_table[0])}')

    if player_one_table[0].value == player_two_table[0].value:
        print('------- War Started -------')
        winner, cards = start_war(player_one_table, player_two_table)
    elif player_one_table[0].value > player_two_table[0].value:
        winner = player_one
        cards = player_one_table + player_two_table
    else:
        winner = player_two
        cards = player_one_table + player_two_table

    if winner == player_one:
        player_one.add_cards(cards)
        print(f'Player 1 Won the following cards {[str(x) for x in cards]}')

    else:
        player_two.add_cards(cards)
        print(f'Player 2 Won the following cards {[str(x) for x in cards]}')


def game_start():
    print('Dealing Cards')
    deal_cards()
    print('Starting Game')
    game_on = True

    while game_on:
        evaluate()
        if len(player_one.deck_of_cards) == 0:
            print('Player Two Won!!!')
            game_on = False
        elif len(player_two.deck_of_cards) == 0:
            print('Player One Won!!!')
            game_on = False

        if not game_on:
            user_choice = ''
            while user_choice != 'y' and user_choice != 'n':
                user_choice = input("Do you want to play again ? y/n")

            if user_choice == 'y':
                player_one.wipe_cards()
                player_two.wipe_cards()
                deal_cards()
                game_on = True
            else:
                break


game_start()
