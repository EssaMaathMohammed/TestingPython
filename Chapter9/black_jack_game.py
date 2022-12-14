"""
this is a code to implement a black jack simple game
"""
from Chapter8.MilestoneProject.DeckOfCards import DeckOfCards
from BJPlayer import BJPlayer

BJ_deck = DeckOfCards()
dealer = BJPlayer('Essa', 'Dealer')
player_one = BJPlayer('Nada', 'Player')


def deal_cards():
    """
    this is a code to implement a black jack simple game
    """
    dealer.add_cards([BJ_deck.pick_card(), BJ_deck.pick_card()])
    dealer.deck_of_cards[1].hidden = True
    player_one.add_cards([BJ_deck.pick_card(), BJ_deck.pick_card()])


def get_total(player):
    """
    this is a code to implement a black jack simple game
    """
    total = 0
    for card in player.deck_of_cards:
        if not card.hidden:
            total += card.value
    return total


def display_table():
    """
    this is a code to implement a black jack simple game
    """
    print('\n\n\n ----- Showing Table ----- \n\n\n')
    print(f'Dealer Hand\n{dealer.print_deck()} \nTotal: {get_total(dealer)}')
    print(f'Player Hand\n{player_one.print_deck()} \nTotal: {get_total(player_one)}')
    print('\n\n\n ----- End Table ----- \n\n\n')


def add_total():
    """
    this is a code to implement a black jack simple game
    """
    return sum(x.value for x in player_one.deck_of_cards), \
           sum(x.value for x in dealer.deck_of_cards)


def clear_table():
    """
    this is a code to implement a black jack simple game
    """
    player_one.remove_cards()
    dealer.remove_cards()


def find_card(player_name):
    for index, card in enumerate(player_name.deck_of_cards):
        if card.rank == 'ace' and card.value == 11:
            return index
    return -1


def show_table():
    """
    this is a code to implement a black jack simple game
    """
    for card in dealer.deck_of_cards:
        card.hidden = False


def start_choice(player_name):
    """
    this is a code to implement a black jack simple game
    """
    if player_name.player_type == 'Player':
        still_choosing = True
        while still_choosing:
            player_choice = ''
            while player_choice not in ('h', 's'):
                player_choice = input('select an action: Hit(h) or Stand(s)')
                if player_choice == 's':
                    return 'stand'
                if player_choice == 'h':
                    player_name.add_cards(BJ_deck.pick_card())
                    display_table()
                    if get_total(player_name) > 21:
                        if find_card(player_name) != -1:
                            player_name.deck_of_cards[find_card(player_name)].value = 1
                            print('Ace Value Changed to 1')
                            display_table()
                        else:
                            return 'bust'
                    if get_total(player_name) == 21:
                        return 'blackjack'
    elif player_name.player_type == 'Dealer':
        show_table()
        print("\n\n ----- Show Hand -----")
        display_table()
        while True:
            if get_total(player_name) > 21:
                if find_card(player_name) != -1:
                    player_name.deck_of_cards[find_card(player_name)].value = 1
                    print('Ace Value Changed to 1')
                    display_table()
                else:
                    return 'bust'
            if get_total(player_name) > 17 or get_total(player_name) > get_total(player_one):
                return 'stand'
            if get_total(player_name) == 21:
                return 'blackjack'

            player_name.add_cards(BJ_deck.pick_card())
            display_table()


def game_start():
    """
    this is a code to implement a black jack simple game
    """
    while True:
        winner = ''
        clear_table()

        BJ_deck.create_deck_of_cards()
        deal_cards()
        display_table()

        player_state = start_choice(player_one)

        if player_state == 'bust':
            winner = dealer
        elif player_state in ('blackjack', 'stand'):
            dealer_state = start_choice(dealer)
            if dealer_state == 'bust':
                winner = player_one
            elif dealer_state in ('blackjack', 'stand'):
                if get_total(player_one) == get_total(dealer) \
                        or get_total(player_one) < get_total(dealer):
                    winner = dealer
                else:
                    winner = player_one

        print(f'winner is {winner}')

        player_choice = ''
        while player_choice not in ('y', 'n'):
            player_choice = input('do you want to play again? y/n')

        if player_choice == 'n':
            break


game_start()
