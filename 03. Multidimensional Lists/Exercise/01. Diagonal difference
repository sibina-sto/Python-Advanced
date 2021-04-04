def get_primary_diagonal_sum(matrix, square_matrix_size):
    primary_diagonal_sum = 0

    for row in range(square_matrix_size):
        col = row
        primary_diagonal_sum += matrix[row][col]

    return primary_diagonal_sum


def get_secondary_diagonal_sum(matrix, square_matrix_size):
    secondary_diagonal_sum = 0

    for row in range(square_matrix_size):
        col = square_matrix_size - 1 - row
        secondary_diagonal_sum += matrix[row][col]

    return secondary_diagonal_sum


def get_absolute_sum_difference(primary_diagonal_sum, secondary_diagonal_sum):
    return abs(primary_diagonal_sum - secondary_diagonal_sum)


square_matrix_size = int(input())
matrix = [list(map(int, input().split())) for _ in range(square_matrix_size)]

primary_diagonal_sum = get_primary_diagonal_sum(matrix, square_matrix_size)
secondary_diagonal_sum = get_secondary_diagonal_sum(matrix, square_matrix_size)
print(get_absolute_sum_difference(primary_diagonal_sum, secondary_diagonal_sum))
