import numpy as np
from fake_localization import *
import math

'''
What?
'''


def find_intersection (vert, hori, botx, boty, botz):
    r = 0.0
    x = botx
    y = boty
    z = botz
    while ( x < 100 and x > 0 and y < 100 and y > 0 and z < 100 and z > 0):
        r = r + 0.5
        x = botx + r * math.sin(vert) * math.cos(hori)
        y = boty + r * math.sin(vert) * math.sin(hori)
        z = botz + r * math.cos(vert)
    # print(x , y , z)
    return x, y, z


def cast_rays(botx, boty, botz):
    xpt = []
    ypt = []
    zpt = []
    for vert in range(-15, 16, 1):
        for hori in range(0, 360, 5):
            x, y, z = find_intersection(vert, hori, botx, boty, botz)
            xpt.append(x)
            ypt.append(y)
            zpt.append(z)
    xpt = np.float32(xpt)
    ypt = np.float32(ypt)
    zpt = np.float32(zpt)
    return xpt, ypt, zpt


def sense(botx, boty, botz):
    xpt, ypt, zpt = cast_rays(botx, boty, botz)
    return xpt, ypt, zpt
