import time
import config
import food


current_direction = config.DIRECTIONS["RIGHT"]
snake_position = [(0, 0), (1, 0), (2, 0)]

ellapsed_time = time.time()
move_seconds = .2  # move every N seconds
move_inc = .01


def draw():
    fill(255)

    for x, y in snake_position:
        rect(x, y, 1, 1)


def move():
    global ellapsed_time

    if time.time() - ellapsed_time < move_seconds:
        return

    ellapsed_time = time.time()

    for i in range(len(snake_position)):
        if i == len(snake_position) - 1:
            x, y = snake_position[i]
            t_x, t_y = config.DIRECTIONS_TRANSFORM[current_direction]
            new_x = x + t_x
            new_y = y + t_y

            if new_x < 0:
                new_x = config.GRID_SIZE
            if new_x > config.GRID_SIZE:
                new_x = 0
            if new_y < 0:
                new_y = config.GRID_SIZE
            if new_y > config.GRID_SIZE:
                new_y = 0

            snake_position[i] = (new_x, new_y)
        else:
            snake_position[i] = snake_position[i+1]


def change_direction(new_direction):
    global current_direction
    current_direction = new_direction


def can_eat_food():
    return snake_position[-1] == food.food_position


def grow():
    global move_seconds, snake_position

    snake_position = [snake_position[0]] + snake_position
    
    if move_seconds - move_inc > 0:
        move_seconds -= move_inc

def is_dead():
    head = snake_position[-1]
    for block in snake_position[:-1]:
        if head == block:
            return True
    return False
