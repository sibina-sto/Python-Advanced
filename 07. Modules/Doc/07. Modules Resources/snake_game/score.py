import os
import config

current_score = 0
current_highscore = 0
score_pos = (10, 25)
highscore_pos = (10, 55)
score_text = "Score: "
highscore_text = "Highscore: "


def draw_score():
    fill(255)
    textSize(24)
    text(score_text + str(current_score),
         score_pos[0],
         score_pos[1])

    text(highscore_text + str(current_highscore),
         highscore_pos[0],
         highscore_pos[1])


def increase():
    global current_score
    current_score += 1


def load_highscore():
    global current_highscore

    if not os.path.exists(config.HIGHSCORE_FILE_PATH):
        return

    with open(config.HIGHSCORE_FILE_PATH, "r") as file:
        current_highscore = int(file.read())

def update_highscore():
    should_update_highscore = current_score > current_highscore
    if should_update_highscore:
        with open(config.HIGHSCORE_FILE_PATH, 'a'):
            pass

        with open(config.HIGHSCORE_FILE_PATH, "w") as file:
            file.write(str(current_score))
