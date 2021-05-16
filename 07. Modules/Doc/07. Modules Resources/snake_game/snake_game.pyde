import config
import snake
import food
import score


def setup():
    frameRate(config.FPS)
    size(config.DISPLAY_SIZE,
         config.DISPLAY_SIZE)
    score.load_highscore()


def draw():
    background(0)

    # Draw stuff
    snake.draw_snake()
    food.draw_food()
    score.draw_score()

    # Update game world
    snake.move()

    if snake.can_eat_food(food.food_pos):
        snake.grow()
        food.respawn()
        score.increase()

    if snake.is_dead():
        print("Game over!")
        score.update_highscore()
        noLoop()


def keyPressed():
    direction = snake.current_direction

    if keyCode == UP and snake.current_direction != config.DIRECTIONS["DOWN"]:
        direction = config.DIRECTIONS["UP"]
    elif keyCode == DOWN and snake.current_direction != config.DIRECTIONS["UP"]:
        direction = config.DIRECTIONS["DOWN"]
    elif keyCode == LEFT and snake.current_direction != config.DIRECTIONS["RIGHT"]:
        direction = config.DIRECTIONS["LEFT"]
    elif keyCode == RIGHT and snake.current_direction != config.DIRECTIONS["LEFT"]:
        direction = config.DIRECTIONS["RIGHT"]

    snake.change_direction(direction)
