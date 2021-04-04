def check_equal_square_chars(matrix, row, col):
    if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
        return True
    return False


def find_equal_squares_count(matrix, rows_count, cols_count):
    equal_square_chars_count = 0

    for row in range(rows_count - 1):
        for col in range(cols_count - 1):
            if check_equal_square_chars(matrix, row, col):
                equal_square_chars_count += 1

    return equal_square_chars_count


rows_count, cols_count = list(map(int, input().split()))
matrix = [input().split() for _ in range(rows_count)]

equal_square_chars_count = find_equal_squares_count(matrix, rows_count, cols_count)

if equal_square_chars_count:
    print(equal_square_chars_count)
else:
    print("No 2 x 2 squares of equal cells exist.")
