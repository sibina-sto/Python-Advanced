def read_int_list_from_input(separator=" "):
    return [int(x) for x in input().split(separator)]


def get_submatrix_sum(matrix, row, col):
    return matrix[row][col] + matrix[row][col + 1] + \
           matrix[row + 1][col] + matrix[row + 1][col + 1]


def print_submatrix(matrix, row, col):
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            print(matrix[r][c], end=" ")
        print()


rows_count, cols_count = read_int_list_from_input(", ")
matrix = [read_int_list_from_input(", ") for _ in range(rows_count)]

max_square_sum = 0
max_square_values = (0, 0)

for row in range(rows_count - 1):
    for col in range(cols_count - 1):
        curr_square_sum = get_submatrix_sum(matrix, row, col)
        if curr_square_sum > max_square_sum:
            max_square_sum = curr_square_sum
            max_square_values = (row, col)


max_row_value, max_col_value = max_square_values
print_submatrix(matrix, max_row_value, max_col_value)
print(max_square_sum)
