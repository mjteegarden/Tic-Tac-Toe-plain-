
# INFORMATION and INSTRUCTIONS for game
'''
TIC-TAC-TOE
The computer plays 'X'; the user plays 'O'
'X' goes first; 'X' always starts in middle of game_board
All the squares are numbered row by row starting with 1
User inputs move by entering number of chosen square (number must be valid)
Program checks if game is over − check these outcomes in this order: 
    computer wins (3 Xs in row)
    user wins (3 Os in row)
    game ends with tie  (all cells full; no wins)
    game continues (not all cells are full yet)
Computer responds with move and check loop is repeated
AI - random field choice made by program
'''


# MODULES to import
import os
import random
import sys


# CELL INFORMATION
# the cells of the game_board (empty, or O, or X)
cell_empty = "[ ]"
cell_O = "[O]"
cell_X = "[X]"
board_full = False
game_ended = False


# each cell has its number (1-9), its coordinates (row, column; each 1-3), and cell status (default: cell_empty)
cell1 = [1, 0, 0, cell_empty]
cell2 = [2, 0, 1, cell_empty]
cell3 = [3, 0, 2, cell_empty]
cell4 = [4, 1, 0, cell_empty]
cell5 = [5, 1, 1, cell_empty]
cell6 = [6, 1, 2, cell_empty]
cell7 = [7, 2, 0, cell_empty]
cell8 = [8, 2, 1, cell_empty]
cell9 = [9, 2, 2, cell_empty]


# prepare screen for game play: (1) screen clearing; (2) pseudo-randomization
# os.system("cls")
random.seed()


# game board is a list of 9 elements; each element is itself a list
game_board = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]


# function displays game_board on-screen
def display_game_board():
    os.system("cls")
    for x in range(9):
        print(game_board[x][3], end="")     # print cells on same line: only element 3 (cell's contents)
        if ((x + 1) % 3) == 0:              # if cell is 3, 6, or 9, make new line
            print()                         # print space afterward


# function checks for victory, tie, or continuing play
def check_victory(game_piece):     # check if game meets victory condition (game_piece is cell_X or cell_O)
    if (game_board[0][3] == game_board[1][3] == game_board[2][3] == game_piece) or\
        (game_board[3][3] == game_board[4][3] == game_board[5][3] == game_piece) or\
        (game_board[6][3] == game_board[7][3] == game_board[8][3] == game_piece) or\
        (game_board[0][3] == game_board[3][3] == game_board[6][3] == game_piece) or\
        (game_board[1][3] == game_board[4][3] == game_board[7][3] == game_piece) or\
        (game_board[2][3] == game_board[5][3] == game_board[8][3] == game_piece) or\
        (game_board[0][3] == game_board[4][3] == game_board[8][3] == game_piece) or\
        (game_board[2][3] == game_board[4][3] == game_board[6][3] == game_piece):
        print("Player ", game_piece, "wins!")
        game_ended = True
        sys.exit()

    else:           # check if tie...all game_board cells are full
        board_full = False
        for cell in range(len(game_board)):
            if game_board[cell][3] != cell_empty:
                board_full == True
                exit
            else:
                board_full == False

        if board_full == True:
            print("It's a tie!")
            game_ended = True
            sys.exit()
        else:
            return False


# MAIN GAME LOOP
# while (no victory or tie yet) is True:
#     computer "X" goes first
#     display_game_board
#     user "O" goes second
#     get user input for turn
# computer checks game's victory condition:
#     Xs win: print Computer-Victory message; exit program
#     Os win: print User-Victory message; exit program
#     Tie: print Tied-No-Victory message; exit program
#     Not done yet: No victory message; continue game loop

while (game_ended) == False:
    
    # COMPUTER PLAYS
    # computer decides which cell to take for "X"; AI uses random choice
    # then display updated game_board
    # then check for victory conditions
    cell_avail = True

    while cell_avail == True:
        comp_choice = random.randint(0, 8)                      # come up with random number 0-8 (1-9 minus 1) 
        if game_board[comp_choice][3] == cell_empty:        # if the chosen cell is empty, use it
            game_board[comp_choice][3] = cell_X             # update game board
            check_victory(cell_X)
            cell_avail = False
            # break
        else: 
            cell_avail = True

    # display_game_board
    display_game_board()


    # USER PLAYS
    # display updated game_board
    # check for victory conditions

    cell_avail = False
    while not (cell_avail):
        user_cell = int((input("Select an empty cell for 'O' [1-9]: ")))
        if (1 <= user_cell <= 9):         # if user_cell is an integer and 1-9
            cell_avail == True
            break
        else:
            cell_avail == False

    # cell_avail = True
    while cell_avail == True:
        if game_board[user_cell - 1][3] == cell_empty:
            game_board[user_cell - 1][3] = cell_O
            check_victory(cell_O)
            cell_avail = False
            # break
        else:
            cell_avail = True


    # display_game_board
    display_game_board()
    #  RETURN TO MAIN GAME LOOP


'''
STUFF TO KEEP:
miscellaneous stuff to keep...maybe to display
vertical_border = "+-------+-------+-------+"
empty_row = "|       |       |       |"
game_board_cells = [[], [], []]     # board[row][column]
'''

'''
TODO list
-- expand display to match cisco academy project
-- 
'''
