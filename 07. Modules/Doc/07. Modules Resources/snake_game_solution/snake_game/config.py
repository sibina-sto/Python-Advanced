FPS = 60

SCREEN_SIZE = 600
SCALE = 20
GRID_SIZE = SCREEN_SIZE // SCALE

DIRECTIONS = {"UP": 0,
              "DOWN": 1,
              "LEFT": 2,
              "RIGHT": 3}

DIRECTIONS_TRANSFORM = {DIRECTIONS["UP"]: (0, -1),
                        DIRECTIONS["DOWN"]: (0, 1),
                        DIRECTIONS["LEFT"]: (-1, 0),
                        DIRECTIONS["RIGHT"]: (1, 0)}
