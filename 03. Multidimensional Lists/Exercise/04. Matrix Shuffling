def validate_indexes(element_position, rows_count, cols_count):
    return 0 <= element_position[0] < rows_count and 0 <= element_position[1] < cols_count


def validate_command_data(command_data, rows_count, cols_count):
    tokens = command_data.split()
    if tokens[0] == "swap" and len(tokens) == 5:
        command, *rows_data = tokens
        first_element_position = [int(rows_data[0]), int(rows_data[1])]
        second_element_position = [int(rows_data[2]), int(rows_data[3])]

        return validate_indexes(first_element_position, rows_count, cols_count) \
               and validate_indexes(second_element_position, rows_count, cols_count)


def swap_matrix_elements(matrix, rows_data):
    first_row, first_col, second_row, second_col = list(map(int, rows_data))
    matrix[first_row][first_col], matrix[second_row][second_col] = matrix[second_row][second_col], \
                                                                   matrix[first_row][first_col]
    return matrix


rows_count, cols_count = list(map(int, input().split()))
matrix = [input().split() for _ in range(rows_count)]

command_data = input()
while not command_data == "END":
    if validate_command_data(command_data, rows_count, cols_count):
        command, *rows_data = command_data.split()
        matrix = swap_matrix_elements(matrix, rows_data)
        [print(' '.join(row)) for row in matrix]
    else:
        print("Invalid input!")

    command_data = input()
