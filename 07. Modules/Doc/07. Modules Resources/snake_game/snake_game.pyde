import config
import snake
import food
import score
import os


def end_screen():
    background(150)
    fill(255)
    textSize(64)
    text(config.GAME_OVER_MESSAGE, config.WINDOW_WIDTH / 2 - len(config.GAME_OVER_MESSAGE) * 15, config.WINDOW_HEIGHT / 2)
    if score.score > score.highscore:
        text(config.HIGH_SCORE_MESSAGE, config.WINDOW_WIDTH / 2 - len(config.HIGH_SCORE_MESSAGE) * 15, config.WINDOW_HEIGHT / 2 + 64)

def setup():
    size(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    frameRate(10)
    
    if os.path.exists(config.HIGHSCORE_FILE_PATH):
        with open(config.HIGHSCORE_FILE_PATH, "r") as file:
            score.highscore = int(file.read())

    food.food_img = loadImage("images/apple.png")
	# load snake images here
    
def draw():
    background(0)
    snake.show()
    snake.move()
    food.show()
    score.show()
    
    if snake.touches_food():
        snake.eat_food()
        food.reset()
        score.score += 1
        
    if snake.eats_self():
        end_screen()
        score.update_highscore()
        noLoop()


def keyPressed():
    if keyCode == UP and config.CURRENT_DIR != "down":
        config.CURRENT_DIR = "up"
    elif keyCode == DOWN and config.CURRENT_DIR != "up":
        config.CURRENT_DIR = "down"
    elif keyCode == LEFT and config.CURRENT_DIR != "right":
        config.CURRENT_DIR = "left"
    elif keyCode == RIGHT and config.CURRENT_DIR != "left":
        config.CURRENT_DIR = "right"
