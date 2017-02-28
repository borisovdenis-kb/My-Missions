from my_missions.config import colors
from random import choice


def get_random_color_set():
    return choice(list(colors.values()))

