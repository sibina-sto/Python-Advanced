def decode_position(position, board_size):
    row = (position - 1) // board_size
    col = (position - 1) % board_size
    return row, col


def all_single_value(ll, mark):
    for cell in ll:
        if not cell == mark:
            return False
    return True
