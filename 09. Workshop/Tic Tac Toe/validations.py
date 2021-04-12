from tic_tac_toe.utils import decode_position


def is_position_valid(position, board):
    board_size = len(board)
    is_in_board = position and 0 < position < 10

    if not is_in_board:
        return False

    row, col = decode_position(position, board_size)
    return board[row][col] is None
