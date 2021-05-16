TEXT_SIZE = 20
TEXT_POSITION = (5, 20)

current_score = 0


def draw():
    x, y = TEXT_POSITION
    fill(255)
    textSize(TEXT_SIZE)
    text("Score: " + str(current_score), x, y)


def increase():
    global current_score
    current_score += 1
