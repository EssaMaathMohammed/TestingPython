"""
this code is used for making a simple Tic_Tac_Toe game
"""

STARTING_PLAYER = 1
tic_tac_toe_list = ['', '', '',
                    '', '', '',
                    '', '', '']
tic_tac_toe_win_dict = {1: [0, 1, 2], 2: [3, 4, 5],
                        3: [6, 7, 8], 4: [0, 3, 6],
                        5: [1, 4, 7], 6: [2, 5, 8],
                        7: [2, 4, 6], 8: [0, 4, 8]}


def check_win(current_mark):
    win_counter = 0
    for _, win_list in tic_tac_toe_win_dict.items():
        for index in win_list:
            if tic_tac_toe_list[index] == current_mark:
                win_counter += 1
        if win_counter == 3:
            display_ttt(tic_tac_toe_list)
            clear_ttt_list()
            return True
        win_counter = 0
    return False


def display_ttt(rows):
    print('\n' + '     |'.center(5) * 2)
    for index, value in enumerate(rows):
        if index % 3 == 0 and index != 0:
            # print('\n' + '     |'.center(5) * 2, end='')
            print('\n__________________', end='')
            print('\n' + '     |'.center(5) * 2 + '\n', end='')
        elif index != 0:
            print('|', end='')
        print(f'{value.center(5)}', end='')
    # print('\n' + '     |'.center(5) * 2)
    print()


def validate_input():
    user_input = input("enter a value between 1 to 9")
    acceptable_range = range(0, 10)
    within_range = False
    while not user_input.isdigit() or not within_range:

        if not user_input.isdigit():
            user_input = input("Please enter a value between 1 to 9")
        elif int(user_input) not in acceptable_range:
            print("The value you entered is out of range")
            user_input = input("Please enter a value between 1 to 9")
        else:
            within_range = True

    return int(user_input) - 1


def submit_user_input(index, value):
    if tic_tac_toe_list[index] != '':
        return False

    tic_tac_toe_list[index] = value
    return True


def check_draw():
    full_spaces = 0
    for item in tic_tac_toe_list:
        if item != '':
            full_spaces += 1
    return full_spaces == 9


def start_game(current_player):
    display_ttt(tic_tac_toe_list)
    allowed_marks = ['X', 'O']
    mark = 'not defined'
    winner = ''
    draw = False
    while mark not in allowed_marks:
        mark = input('select X or O to be the first player').upper()

    # start playing the game
    playing = True
    while playing and not draw:

        valid = submit_user_input(validate_input(), mark)
        while not valid:
            print('\nthis place is already taken please choose another place')
            valid = submit_user_input(validate_input(), mark)

        if check_win(mark):
            playing = False
            winner = current_player
            print(f'Game Ended Player {current_player} Won!')
            while True:
                user_input = input("Do you want to play again? y/n")
                if user_input == 'y':
                    playing = True
                    break
                if user_input == 'n':
                    break
                print('please enter a valid input y/n')
            if playing:
                if winner == 1:
                    current_player = 2
                else:
                    current_player = 1
                print(f'Playing Again, Player {current_player} starting first')

            if check_draw():
                print('Game Ended nobody Won! ggz')
                playing = False
                while True:
                    user_input = input("Do you want to play again? y/n")
                    if user_input == 'y':
                        playing = True
                        break
                    if user_input == 'n':
                        break
                    print('please enter a valid input y/n')
                    print(f'Playing Again, Player {current_player} starting first')

        if mark == allowed_marks[0]:
            mark = allowed_marks[1]
        else:
            mark = allowed_marks[0]

        current_player = switch_player(current_player)


def switch_player(player):
    if player == 1:
        player = 2
    else:
        player = 1
    display_ttt(tic_tac_toe_list)
    return player


def clear_ttt_list():
    for index, _ in enumerate(tic_tac_toe_list):
        tic_tac_toe_list[index] = ''


print("Starting Game")
start_game(STARTING_PLAYER)
