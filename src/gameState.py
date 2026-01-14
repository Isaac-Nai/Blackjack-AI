from enum import Enum

class gameState(Enum):
    START = 1
    DEALING = 2
    PLAYER_TURN = 3
    AI_TURN = 4
    RESOLVE = 5
    END = 6
