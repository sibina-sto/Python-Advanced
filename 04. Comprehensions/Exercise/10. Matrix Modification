def validate_coordinates(row, col):
    return 0 <= row < matrix_size and 0 <= col < matrix_size


matrix_size = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(matrix_size)]

line = input()
while not line == "END":
    command, row, col, value = line.split()
    row = int(row)
    col = int(col)
    value = int(value)

    if validate_coordinates(row, col):
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    line = input()

[print(' '.join([str(num) for num in row])) for row in matrix]
