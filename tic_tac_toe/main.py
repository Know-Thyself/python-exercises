def welcome_display():
    print('Welcome to Tic Tac Toe Board Game!')
    display_board(['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'])
    game_setup([' '] * 10)


def display_board(board):
    rows = [board[1:4], board[4:7], board[7:]]
    list(map(display_row, rows))


def display_row(row):
    for index, item in enumerate(row):
        if index == 0:
            print('|' + item + '|', end="")
        elif index == 1:
            print(item + '|', end="")
        else:
            print(item + '|')


def game_setup(board):
    print('Current Board:')
    display_board(board)
    player_input(board)


def player_input(board):
    # Player one gets to choose marker
    player_one, player_two = validate_player_marker()
    # Player two gets to make the first move
    player_two_position = validate_players_move(player_two)
    board[player_two_position] = player_two
    display_board(board)
    next_player(player_one, board)


def validate_player_marker():
    player_one = ''
    player_two = ''
    while player_one not in ['X', 'O']:
        player_one = input('Please enter "X" or "O" as your marker: ').upper()
        if player_one == 'X':
            player_two = 'O'
        else:
            player_two = 'X'
    return player_one, player_two


def validate_players_move(player):
    player_position = 'Not a number'
    while player_position not in range(1, 10):
        player_position = input(
            f'You are {player}. Please chose your position (1 - 9): ')
        if player_position.isnumeric():
            player_position = int(player_position)
    return player_position


def next_player(player, board):
    player_position = validate_players_move(player)
    board[player_position] = player
    display_board(board)
    game_status(player, board)


def game_status(player, board):
    # Check if either vertical, horizontal or diagonal lines values are identical
    if does_win(board[1:4]) \
            or does_win(board[4:7]) \
            or does_win(board[7:]) \
            or does_win(board[1:8:3]) \
            or does_win(board[2:9:3]) \
            or does_win(board[3::3]) \
            or does_win(board[1::4]) \
            or does_win(board[3:8:2]):
        print(f'Player {player} wins!')
        play_again = input('Enter "Y" to play again or "N" to exit: ').lower()
        if play_again == 'y':
            reset()
    elif ' ' not in board[1:]:
        print("It's a cat's game! No one wins.")
        play_again = input('Enter "Y" to play again or "N" to exit: ').lower()
        if play_again == 'y':
            reset()
    else:
        if player == 'X':
            next_player('O', board)
        else:
            next_player('X', board)


def does_win(lst):
    """
    Takes in a list and checks if all values in a list are identical
    :param lst:
    :return: bool
    """
    if lst[0] != ' ':
        return all(i == lst[0] for i in lst)
    else:
        return False


def reset():
    game_setup([' '] * 10)


if __name__ == '__main__':
    welcome_display()
