# board
# display board
# play game
# handle turn
# check win
# check rows/columns/diagonal
# check tie
# flip player

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_runs: True
winner = "winner"
current_player = "X"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def turn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1-9:")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", ]:
            position = input("Invalid input! Choose a position from 1-9:")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        elif board[position]:
            print("Space is taken.Please try again.")


    board[position] = player
    display_board()

def play_game():
    game_runs = True

    display_board()
    while game_runs:
        turn(current_player)
        check_if_gameover()
        flip_player()



def check_if_gameover():
    check_win()
    check_tie()
    if winner == "X" or winner == "O":
        print("Player " + winner + " won!")
    elif winner == None:
        print("Tie.")
    pass


def check_win():
    # set up global variables from up top
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    if column_winner:
        winner = column_winner
    if diagonal_winner:
        winner = diagonal_winner

    return


def check_rows():
    global game_runs
    # check if rows are the same and not a dash
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_runs = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_runs
    # check if columns are the same and not a dash
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_runs = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    global game_runs
    # check if diagonal are the same and not a dash
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_runs = False
        return board[4]
    return


def check_tie():
    global game_runs
    if "-" not in board:
        game_runs = False
    return

def flip_player():
    # x to o be mindful of the == , and =
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return




play_game()
