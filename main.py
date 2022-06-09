# CSE 210-13
# W01 Intro Ponder & Prove - Tic Tac Toe
# Author: Scott LeFoll
# 06/08/22

"""
Tic-Tac-Toe
Love is a game of tic-tac-toe,
Constantly waiting for the next x or o.
- Lang Leav -

Overview
Tic-Tac-Toe is a game in which two players seek in alternate turns to
complete a row, a column, or a diagonal with either three x's or three o's
drawn in the spaces of a grid of nine squares.

Rules
Tic-Tac-Toe is played according to the following rules.

The game is played on a grid that is three squares by three squares.
Player one uses x's. Player two uses o's.
Players take turns putting their marks in empty squares.
The first player to get three of their marks in a row (vertically, horizontally,
or diagonally) is the winner. If all nine squares are full and neither player
has three in a row, the game ends in a draw.

Interface

1|2|3
-+-+-
4|5|6
-+-+-
7|8|9

x's turn to choose a square (1-9): 2

1|x|3
-+-+-
4|5|6
-+-+-
7|8|9

o's turn to choose a square (1-9): 5

1|x|3
-+-+-
4|o|6
-+-+-
7|8|9

x's turn to choose a square (1-9): _

...

x|x|x
-+-+-
4|o|6
-+-+-
7|8|o

Good game. Thanks for playing!
> _
Requirements
Your program must also meet the following requirements.

The program must have a comment with assignment and author names.
The program must have at least one if/then block.
The program must have at least one while loop.
The program must have more than one function.
The program must have a function called main.

Suggestions

Make the game in any way you like. A few ideas are as follows.

Enhanced input validation with user-friendly messages.
Enhanced game over messages (x's, o's or draw).
Enhanced board size (4x4, 5x5, 6x6 grid, or user selected!)
Enhanced game display (different colors for each player)"""

# from termcolor import colored
from colorama import Fore, Back, Style
from colorama import init
# from blessings import terminal
# from stringcolor import *
# from ansiwrap import *

# X_text = Fore.RED + 'X' + Style.RESET_ALL

X_WINNER_MSG = Fore.MAGENTA + """ 
                                                                                                                              
 .oPYo. 8                               o    o     o            o  8               o      o  o                          88 88 
 8    8 8                               `b  d'                  8  8               8      8                             88 88 
o8YooP' 8 .oPYo. o    o .oPYo. oPYo.     `bd'     o8 .oPYo.    o8P 8oPYo. .oPYo.   8      8 o8 odYo. odYo. .oPYo. oPYo. 88 88 
 8      8 .oooo8 8    8 8oooo8 8  `'     .PY.      8 Yb..       8  8    8 8oooo8   8  db  8  8 8' `8 8' `8 8oooo8 8  `' 88 88 
 8      8 8    8 8    8 8.     8        .P  Y.     8   'Yb.     8  8    8 8.       `b.PY.d'  8 8   8 8   8 8.     8     `' `' 
 8      8 `YooP8 `YooP8 `Yooo' 8       .P    Y.    8 `YooP'     8  8    8 `Yooo'    `8  8'   8 8   8 8   8 `Yooo' 8     88 88 
:..:::::..:.....::....8 :.....:..::::::..::::..::::..:.....:::::..:..:::..:.....:::::..:..:::....::....::..:.....:..::::......
:::::::::::::::::::ooP'.::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::...::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""+ Style.RESET_ALL

O_WINNER_MSG = Fore.CYAN + """                                                                                                                            
 .oPYo. 8                              .oPYo.    o            o  8               o      o  o                          88 88 
 8    8 8                              8    8                 8  8               8      8                             88 88 
o8YooP' 8 .oPYo. o    o .oPYo. oPYo.   8    8   o8 .oPYo.    o8P 8oPYo. .oPYo.   8      8 o8 odYo. odYo. .oPYo. oPYo. 88 88 
 8      8 .oooo8 8    8 8oooo8 8  `'   8    8    8 Yb..       8  8    8 8oooo8   8  db  8  8 8' `8 8' `8 8oooo8 8  `' 88 88 
 8      8 8    8 8    8 8.     8       8    8    8   'Yb.     8  8    8 8.       `b.PY.d'  8 8   8 8   8 8.     8     `' `' 
 8      8 `YooP8 `YooP8 `Yooo' 8       `YooP'    8 `YooP'     8  8    8 `Yooo'    `8  8'   8 8   8 8   8 `Yooo' 8     88 88 
:..:::::..:.....::....8 :.....:..:::::::.....::::..:.....:::::..:..:::..:.....:::::..:..:::....::....::..:.....:..::::......
:::::::::::::::::::ooP'.::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::...:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 
"""+ Style.RESET_ALL


def init_game():
    print("Welcome to Tic Tac Toe")
    print()
    X_moves = []
    O_moves = []
    free_squares = [1,2,3,4,5,6,7,8,9]
    wins = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], 
            [1,5,9], [3,5,7]]
    return X_moves, O_moves, free_squares, wins


def check_win(get_move_lst, init_game_lst):
    user_mark = get_move_lst[0]
    move = get_move_lst[1]
    # winning rows are 0 - 8. Win_row 99 is a flag for None.
    win_row = 99
    win = False
    if user_mark == "X":
        for i in range(0, len(init_game_lst[3])):
            # for n in range(0, len(init_game_lst[3][i]-1)):
            # check if any of the "win" combinations are in X's move list - init_game_lst[0]
            if all(moves in init_game_lst[3][i] for moves in init_game_lst[0]):
                win = True
                win_row = i
                return win, win_row, user_mark

    elif user_mark == "O":
        for i in range(0, len(init_game_lst[3])):
            # for n in range(0, len(init_game_lst[3][i]-1)):
            # check if any of the "win" combinations are in O's move list - init_game_lst[1]
            if all(moves in init_game_lst[3][i] for moves in init_game_lst[1]):
                win = True
                win_row = i
                return win, win_row, user_mark

    return False, 99, "X"


def quit_game(game_status, init_game_lst, check_win_lst):

    print()
    draw_board(init_game_lst, check_win_lst)
    print()

    match game_status:
        case "Win":
            if check_win_lst[2] == "X":
                print(X_WINNER_MSG)
            else:
                print(O_WINNER_MSG)
            print()
            print(f"Congratulations player {check_win_lst[2]}!")
        case "Draw":
            print(f"The game is a draw.")
        case "Quit":
            print("One of the players pressed Quit.")
    
    print()
    print("Good game. Thanks for playing!")
    exit()


def get_move(init_game_lst, turn):
    # write validation for input
    move = 99
    user_mark = "X"

    if turn % 2 == 0:
        user_mark = "O"
        print("O's turn.")
    else:
        user_mark = "X"
        print("X's turn.")

    while True:
        try:
            print()
            move = int(input(f"Please choose a free square {init_game_lst[2]}: "))
        except ValueError:
            # if move == "Q" or move == "q": return 101
            print("That is not a valid choice.")
            continue
        else:
            if move < 1 or move > 9:
                print("That is not a valid choice.")
                continue
            elif move not in init_game_lst[2]:
                print("That square is already taken.")
                continue
            else:
                return user_mark, move


def write_move(get_move_lst, init_game_lst, turn):
    user_mark = get_move_lst[0]
    move = get_move_lst[1]

    if user_mark == "X":
        init_game_lst[0].append(move)
        init_game_lst[2].remove(move)
        if len(init_game_lst[0]) < 3: return False, 99, 'X'
    elif user_mark == "O":
        init_game_lst[1].append(move)
        init_game_lst[2].remove(move)
        if len(init_game_lst[1]) < 3: return False, 99, 'O'
    
    print(f"X moves = {get_move_lst[0]}")
    print(f"O moves = {get_move_lst[1]}")
    print()
    return check_win(get_move_lst, init_game_lst)


def draw_board(init_game_lst, check_win_lst):
    # The structure of the check_win_lst is [True, win_row, user_mark]
    X_moves = init_game_lst[0]
    O_moves = init_game_lst[1]

    board = """
          1  |  2  |  3
        -----+-----+-----
          4  |  5  |  6
        -----+-----+-----
          7  |  8  |  9"""


    # X_text = Fore.RED + 'X' + Style.RESET_ALL
    X_text = "X"
    # O_text = Fore.GREEN + 'O' + Style.RESET_ALL
    O_text = "O"

    for i in range(0, len(X_moves)):
        board = board.replace(str(X_moves[i]), X_text)

    for i in range(0, len(O_moves)):
        board = board.replace(str(O_moves[i]), O_text)

    print()
    print(board)
    print()




def main():
    init()
    turn = 0
    win = False
    move = 0
    user_mark = ""
    check_win_lst = [False, 99, "X"]
    # move is set to '101' as a 'Quit' flag.
    init_game_lst = init_game()

    # continue making moves until a win or a draw, or someone quits
    while move != 101 and not win and turn != 10:
        turn += 1
        draw_board(init_game_lst, check_win_lst)
        get_move_lst = get_move(init_game_lst, turn)
        check_win_lst = write_move(get_move_lst, init_game_lst, turn)
        # if Quit flag is set, exit game
        if move == 101: quit_game("Quit", init_game_lst, check_win_lst)
        # check_win_lst[] structure is win, win_row, user_mark
        # if win == True then quit and print win message
        if check_win_lst[0]: quit_game("Win", init_game_lst, check_win_lst)
        # if win == False and board is full, draw
        if turn == 9: quit_game("Draw", init_game_lst, check_win_lst)


if __name__ == "__main__":
    main()
