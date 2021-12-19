import os

from .level import Level
from tiles import sprites

def parse_level(lines):
    lines = list(filter(lambda s: s != '', map(str.strip, lines)))
    return []




def load():
    path = 'level/levels'
    filenames = os.listdir(path)
    levels = []
    for filename in filenames:
        with open(path + '/' + filename, 'r') as file:
            levels.append(parse_level(file.readlines()))


load()