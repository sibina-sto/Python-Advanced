def validate_position(row, col, size):
    return 0 <= row < size and 0 <= col < size


def explode_bomb(damage, matrix, row, col, size):
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if validate_position(r, c, size) and matrix[r][c] > 0:
                matrix[r][c] -= damage

    return matrix


def find_alive_cells(matrix_size, matrix):
    alive_cells = []

    for row in range(matrix_size):
        for col in range(matrix_size):
            cell = matrix[row][col]
            if cell > 0:
                alive_cells += [cell]

    return alive_cells


matrix_size = int(input())
matrix = [list(map(int, input().split())) for _ in range(matrix_size)]
bombs_coordinates = input().split()

for bomb in bombs_coordinates:
    row, col = list(map(int, bomb.split(",")))
    damage = matrix[row][col]
    if damage > 0:
        matrix = explode_bomb(damage, matrix, row, col, matrix_size)


alive_cells = find_alive_cells(matrix_size, matrix)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(' '.join(map(str, row))) for row in matrix]
