from collections import deque

rows_count, cols_count = list(map(int, input().split()))
snake = deque(input())

isle = [[""] * cols_count for _ in range(rows_count)]


for row in range(rows_count):
    for col in range(cols_count):
        curr_col = col
        curr_char = snake.popleft()
        if row % 2 == 1:
            curr_col = cols_count - 1 - col
        isle[row][curr_col] = curr_char
        snake.append(curr_char)


[print(''.join(row)) for row in isle]
