def validate_position(curr_position, board_size):
    row, col = curr_position
    return 0 <= row < board_size and 0 <= col < board_size


def calculate_knight_damage(board, row, col, board_size):
    damage = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]

    for i in range(len(rows)):
        curr_position = [row + rows[i], col + cols[i]]
        if validate_position(curr_position, board_size) and board[curr_position[0]][curr_position[1]] == "K":
            damage += 1

    return damage


board_size = int(input())
board = [list(input()) for _ in range(board_size)]
killed_knights_count = 0

while True:
    knight_most_damage = 0
    knight_to_remove_position = (0, 0)

    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == "K":
                knight_damage = calculate_knight_damage(board, row, col, board_size)
                if knight_damage > knight_most_damage:
                    knight_most_damage = knight_damage
                    knight_to_remove_position = (row, col)

    if knight_most_damage == 0:
        break

    row_to_remove, col_to_remove = knight_to_remove_position
    board[row_to_remove][col_to_remove] = "0"
    killed_knights_count += 1


print(killed_knights_count)
