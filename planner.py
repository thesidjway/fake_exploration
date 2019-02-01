import numpy as np


class Planner(object):
    def __init__(self):
        self.goal = np.zeros((3))

    def iterate_planner(self, map, botx, boty, botz):
        newx = botx
        newy = boty
        newz = botz
        return newx, newy, newz



