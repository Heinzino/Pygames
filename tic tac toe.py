#board
#display board
#play game
#handle turn
#check win
    #check rows/columns/diagonal
#check tie
#flip player

board = ["-","-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_runs:True
winner = "winner"
current_player = "X"

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def play_game():
    display_board()
    while game_runs:
        turn(current_player)
        check_if_gameover()
        flip_player()


def check_if_gameover():
    check_win()
    check_tie()
    pass

def check_win():
    #check rows/diagonals/column
    if winner == "x" or winner == "O":
        print(winner + "won!")
    return

def check_rows():

def check_columns():

def check_diagonals():

def check_tie():
    if winner == None:
        print("Tie.")
    return

def flip_player():
    #x to o
    return
def game_runs():
    return

def current_player():
    return

def turn(current_player):
    position = input("Choose a position from 1-9:")
    position = int(position) - 1
    board[position] = "X"
    display_board()

play_game()