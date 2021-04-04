def find_symbol(matrix, symbol):

    for row in range(matrix_size):
        for col in range(matrix_size):
            curr_symbol = matrix[row][col]
            if curr_symbol == search_symbol:
                return row, col


matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    row = list(input())
    matrix.append(row)

search_symbol = input()
result = find_symbol(matrix, search_symbol)

if result:
    (row, col) = result
    print(f"({row}, {col})")
else:
    print(f"{search_symbol} does not occur in the matrix")
