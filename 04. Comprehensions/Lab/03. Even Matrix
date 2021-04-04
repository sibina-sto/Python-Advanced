def get_filtered_row(row):
    return [num for num in row if num % 2 == 0]


rows_count = int(input())
matrix = [list(map(int, input().split(", "))) for _ in range(rows_count)]
even_nums_matrix = [get_filtered_row(row) for row in matrix]
print(even_nums_matrix)
