def reset_board():
    return [' '] * 9


game_board = reset_board()
game_on = True


def display(board):
    print('{}|{}|{}'.format(board[0], board[1], board[2]))
    print('-----')
    print('{}|{}|{}'.format(board[3], board[4], board[5]))
    print('-----')
    print('{}|{}|{}'.format(board[6], board[7], board[8]))


def player_input():
    marker = 'Wrong'
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose your marker: X or O: ")

    temp_player1: str = marker
    temp_player2 = 'X' if temp_player1 == 'O' else '0'

    return temp_player1, temp_player2


def position_selection(player):
    position_choice = ''
    while not position_choice.isdigit():
        position_choice = input("Player{}: Please enter a position in digit in [1, 9]: ".format(player))

        if not position_choice.isdigit():
            print("Please enter value as numeric digits")
        else:
            pos = int(position_choice)
            if pos not in range(1, 10):
                print("Please enter value as numeric digit in the range 1 to 9")
                position_choice = ''
            elif game_board[pos - 1] != ' ':
                print("Already choosen")
                position_choice = ''

    return int(position_choice) - 1


def game_on_choice():
    choice = ""
    while choice not in ['Y', 'N']:
        choice = input("Do you want to continue the game: ")

    if choice == 'Y':
        return True
    else:
        return False


def all_win(func, input_list): return len(list(filter(func, input_list))) == len(input_list)


def check_for_row_win():
    for i in range(0, 7, 3):
        input_list = game_board[i: i + 3]
        print(input_list)
        if all_win(lambda x: x == 'X', input_list) or all_win(lambda x: x == 'O', input_list):
            return True
    return False


def check_for_col_win():
    for i in range(0, 3):
        input_list = game_board[i: i + (3 * 2) + 1: 3]
        if all_win(lambda x: x == 'X', input_list) or all_win(lambda x: x == 'O', input_list):
            return True
    return False


def check_for_diagonal_win():
    input_list = game_board[0: len(game_board): 4]
    if all_win(lambda x: x == 'X', input_list) or all_win(lambda x: x == 'O', input_list):
        return True
    input_list = game_board[2: (3 * 2) + 1: 2]
    if all_win(lambda x: x == 'X', input_list) or all_win(lambda x: x == 'O', input_list):
        return True
    return False


def check_for_win():
    return check_for_row_win() or check_for_col_win() or check_for_diagonal_win()


def is_board_full():
    return all_win(lambda x: x != ' ', game_board)


while True:
    game_board = reset_board()
    display(game_board)
    player1, player2 = player_input()
    while game_on:
        player1_pos = position_selection(1)
        game_board[player1_pos] = player1

        display(game_board)
        if check_for_win():
            print("Player 1 won")
            break
        elif is_board_full():
            print("Tie")
            break

        player2_pos = position_selection(2)
        game_board[player2_pos] = player2

        display(game_board)

        if check_for_win():
            print("Player 1 won")
            break
        elif is_board_full():
            print("Tie")
            break

    if not game_on_choice():
        break
