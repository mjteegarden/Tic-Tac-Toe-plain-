
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


# Game board status; game status
game_ended = False


# CELL INFORMATION
cell_empty = "[ ]"
cell_O = "[O]"
cell_X = "[X]"


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


# prepare pseudo-randomization for game play
random.seed()


# game board is a list of 9 elements; each element is itself a list
game_board = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]


# function displays game_board on-screen
def display_game_board():
    os.system("cls")
    for x in range(len(game_board)):
        print(game_board[x][3], end="")     # print cells on same line: only element 3 (cell's contents)
        if ((x + 1) % 3) == 0:              # at every 3rd cell (3, 6, 9), make new line
            print()                         # print space afterward


# function checks for victory, tie, or continuing play
def check_victory(game_piece):     # check if cell_X or cell_O meets victory condition
    global game_ended
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if game_board[combo[0]][3] == game_board[combo[1]][3] == game_board[combo[2]][3] == game_piece:
            print(f"Player {game_piece} wins!")
            game_ended = True
            return True
    return False


def check_tie():
    for cell in game_board:
        if cell[3] == cell_empty:
            return False
    print("It's a tie!")
    return True


# MAIN GAME LOOP
#     computer "X" goes first
#     display_game_board
#     user "O" goes second
#     get user input for turn
# computer checks game's victory condition:
#     Xs win: print Computer-Victory message; exit program
#     Os win: print User-Victory message; exit program
#     Tie: print Tied-No-Victory message; exit program
#     Not done yet: No victory message; continue game loop


while not game_ended:
    # COMPUTER PLAYS
    # computer decides which cell to take for "X"; AI uses random choice
    # then display updated game_board
    # then check for victory conditions

    while True:
        comp_choice = random.randint(0, 8)                      # come up with random number 0-8 (1-9 minus 1) 
        if game_board[comp_choice][3] == cell_empty:        # if the chosen cell is empty, use it
            game_board[comp_choice][3] = cell_X             # update game board
            display_game_board()            
            if check_victory(cell_X):
                game_ended = True
                break
            if check_tie():
                game_ended = True
                break
        break
            


    # USER PLAYS
    # display updated game_board
    # check for victory conditions

    while True:
        user_input = (input("Select an empty cell [1-9] for O: "))
        try:
            user_cell = int(user_input) - 1
            if 0 <= user_cell <= 8 and game_board[user_cell][3] == cell_empty:
                game_board[user_cell][3] = cell_O
                display_game_board
                if check_victory(cell_O):
                    game_ended = True
                    break
                if check_tie():
                    game_ended = True
                    break        
                break

            else: 
                print("Select an empty cell [1-9] for O: ")

        except ValueError:
            print("Select an empty cell [1-9] for O.")


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
-- remove the 'coordinate' elements from cells; elements 1 and 2 in each cell 
--      (they're unnecessary) (or make use of them)
-- expand display to match cisco academy project
# TO-DO - change the game_board list to a tuple (but keep individual cell lists as-is)

'''