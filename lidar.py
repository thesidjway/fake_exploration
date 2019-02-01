import numpy as np
from fake_localization import *
import math


class Lidar(object):
    def __init__(self):
        self.vertmin = -5
        self.vertmax = 6
        self.horimin = 0
        self.horimax = 360
        self.horires = 5
        self.vertres = 1
        self.roomsize = 100

    def find_intersection (self, vert, hori, room, botx, boty, botz):
        r = 0.0
        x = botx
        y = boty
        z = botz
        while x < self.roomsize and x > 0 and y < self.roomsize and y > 0 and z < self.roomsize and z > 0:
            r = r + 0.5
            x = botx + r * math.sin(vert) * math.cos(hori)
            y = boty + r * math.sin(vert) * math.sin(hori)
            z = botz + r * math.cos(vert)
            if room.intersection(int(x), int(y), int(z)):
                return x, y, z
        return -1, -1, -1

    def cast_rays(self, room, botx, boty, botz):
        xpt = []
        ypt = []
        zpt = []
        for vert in range(self.vertmin, self.vertmax, self.vertres):
            for hori in range(self.horimin, self.horimax, self.horires):
                x, y, z = self.find_intersection(vert, hori, room, botx, boty, botz)
                if x is not -1:
                    xpt.append(x)
                    ypt.append(y)
                    zpt.append(z)
        xpt = np.float32(xpt)
        ypt = np.float32(ypt)
        zpt = np.float32(zpt)
        return xpt, ypt, zpt

    def sense(self, room, botx, boty, botz):
        xpt, ypt, zpt = self.cast_rays(room, botx, boty, botz)
        return xpt, ypt, zpt
