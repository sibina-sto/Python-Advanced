def is_valid(pos, size):
    return 0 <= pos[0] < size and 0 <= pos[1] < size
 
 
initial_string = [x for x in input()]
 
n = int(input())
 
matrix = []
player_pos = []
directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
 
for row in range(n):
    line = [x for x in input()]
    for col in range(n):
        if line[col] == "P":
            player_pos = [row, col]
    matrix.append(line)
 
m = int(input())
 
for _ in range(m):
    command = input()
    dir_changes = directions[command]
    new_pos = [player_pos[0] + dir_changes[0], player_pos[1] + dir_changes[1]]
 
    if is_valid(new_pos, n):
        matrix[player_pos[0]][player_pos[1]] = "-"
        element = matrix[new_pos[0]][new_pos[1]]
        if element != "-":
            initial_string.append(element)
        player_pos = new_pos
        matrix[player_pos[0]][player_pos[1]] = "P"
 
    else:
        if initial_string:
            initial_string.pop()
 
 
print("".join(initial_string))
[print("".join(row)) for row in matrix]
