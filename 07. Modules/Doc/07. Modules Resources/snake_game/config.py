FPS = 60

DISPLAY_SIZE = 600

SCALE = 40

GRID_SIZE = DISPLAY_SIZE // SCALE

DIRECTIONS = {"UP": 0,
              "DOWN": 1,
              "LEFT": 2,
              "RIGHT": 3}

DIRECTIONS_TRANSFORM = {DIRECTIONS["UP"]: [0, -1],
                        DIRECTIONS["DOWN"]: [0, 1],
                        DIRECTIONS["LEFT"]: [-1, 0],
                        DIRECTIONS["RIGHT"]: [1, 0]}

HIGHSCORE_FILE_PATH = "highscore.txt"

INITIAL_SPEED = .5
SPEED_INC = .1
