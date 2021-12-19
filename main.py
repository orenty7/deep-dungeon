from engine import Engine
from enums import Key
from level import levels
from player import Player
from tile_loader import *

level = levels[0]
level.init_engine((64 * 20, 64 * 12))

level.play()

FPS = 120


