def read_int_list_from_input(separator=" "):
    return [int(x) for x in input().split(separator)]


rows_count, cols_count = read_int_list_from_input(", ")
matrix = []


for _ in range(rows_count):
    row = read_int_list_from_input()
    matrix.append(row)


col_sum = 0
for col in range(cols_count):
    for row in range(rows_count):
        col_sum += matrix[row][col]
    print(col_sum)
    col_sum = 0
