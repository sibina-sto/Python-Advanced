def get_submatrix(cols_count, row):
    return [chr(row) + chr(row + col) + chr(row) for col in range(cols_count)]


rows_count, cols_count = [int(num) for num in input().split()]

matrix = [get_submatrix(cols_count, row) for row in range(97, 97 + rows_count)]
[print(' '.join(row)) for row in matrix]
