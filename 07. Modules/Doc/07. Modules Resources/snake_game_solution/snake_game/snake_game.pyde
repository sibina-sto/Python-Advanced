import config
import snake
import food
import score


current_direction = config.DIRECTIONS["RIGHT"]


def setup():
    size(config.SCREEN_SIZE, config.SCREEN_SIZE)
    frameRate(config.FPS)

def draw():
    background(0)

    # Draw everything in the game
    pushMatrix()
    translate(0, 0)
    scale(config.SCALE)
    strokeWeight(1 / config.SCALE)
    
    snake.draw()
    food.draw()
    
    popMatrix()

    score.draw()

    # Update game world
    snake.change_direction(current_direction)
    snake.move()

    if snake.can_eat_food():
        snake.grow()
        food.respawn()
        score.increase()

    if snake.is_dead():
        print("Game over...")
        noLoop()


def keyPressed():
    global current_direction

    if keyCode == UP and snake.current_direction != config.DIRECTIONS["DOWN"]:
        current_direction = config.DIRECTIONS["UP"]
    elif keyCode == DOWN and snake.current_direction != config.DIRECTIONS["UP"]:
        current_direction = config.DIRECTIONS["DOWN"]
    elif keyCode == LEFT and snake.current_direction != config.DIRECTIONS["RIGHT"]:
        current_direction = config.DIRECTIONS["LEFT"]
    elif keyCode == RIGHT and snake.current_direction != config.DIRECTIONS["LEFT"]:
        current_direction = config.DIRECTIONS["RIGHT"]
