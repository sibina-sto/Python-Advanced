from math import ceil
from my_modules.modules import MustBeXorO, ValueMustBeInRange, PositionOccupied

def check(board, player):
    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]
    cols = [[board[k][i] for k in range(3)] for i in range(3)]
    for i in range(3):
        cols[i] = [max(cols[i].count("X"), cols[i].count("O"))]
    if (diag1.count("X") == 3 or diag1.count("O") == 3 or
            diag2.count("X") == 3 or diag2.count("O") == 3 or
            3 in [board[i].count("X") for i in range(3)] or 3 in [board[i].count("O") for i in range(3)] or
            3 in [num for row in cols for num in row]):
        return True, player
    if " " not in [num for row in board for num in row]:
        return True, "Draw"
    return False, player


def game(row, col, board, symbol):
    if board[row][col] in "XO":
        raise PositionOccupied
    if 0 <= row < 3 and -1 <= col < 3:
        board[row][col] = symbol
    else:
        raise ValueMustBeInRange
    return board


def draw_board(board):
    for row in board:
        print("|  ", end="")
        print('  |  '.join([i for i in row]), end="")
        print('  |')


board = [[" " for i in range(3)] for k in range(3)]
player_1 = input("\n\nPlayer one name: ")
player_2 = input("\nPlayer two name: ")
player_1_symbol = input(f"\n{player_1} would you like to play with 'X' or 'O'? ")
if player_1_symbol not in "XO":
    raise MustBeXorO
player_2_symbol = "X" if player_1_symbol == "O" else "O"
print("\nThis is the numeration of the board")
print("\n|  1  |  2  |  3  |\n|  4  |  5  |  6  |\n|  7  |  8  |  9  |")
print(f"\n{player_1} starts first!")
winner = None
while True:
    player_1_move = int(input(f"\n{player_1} choose a free position [1-9]: "))
    board = game(ceil(player_1_move / 3) - 1, player_1_move % 3 - 1, board, player_1_symbol)
    draw_board(board)
    status = (check(board, player_1))
    if status[0]:
        winner = player_1 if status[1] == player_1 else "Draw"
        break
    player_2_move = int(input(f"\n{player_2} choose a free position [1-9]: "))
    board = game(ceil(player_2_move / 3) - 1, player_2_move % 3 - 1, board, player_2_symbol)
    draw_board(board)
    status = (check(board, player_2))
    if status[0]:
        winner = player_2 if status[1] == player_2 else "Draw"
        break
print(f"{winner} won!" if winner != "Draw" else "Draw!")
