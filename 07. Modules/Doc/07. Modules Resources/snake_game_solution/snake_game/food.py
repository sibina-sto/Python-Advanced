import config


def get_random_coord():
    return floor(random(0, config.GRID_SIZE))


def get_food_location():
    return (get_random_coord(), get_random_coord())


food_position = get_food_location()


def draw():
    x, y = food_position
    fill(0, 255, 0)
    rect(x, y, 1, 1)


def respawn():
    global food_position
    food_position = get_food_location()
