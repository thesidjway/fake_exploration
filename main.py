from lidar import *
from room import *
from mapping import *
from fake_localization import *
import matplotlib.pyplot as plt
import time
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

localization = FakeLocalization(50, 50, 10)  # starting position in x,y,z
room = Room()
lidar = Lidar()
mapper = Mapping()


for i in range(5):
    localization.update_position(10 * i + 1, i * i + 1, 2 * i * i + 1)
    botx, boty, botz = localization.get_curr_estimate()
    xpt, ypt, zpt = lidar.sense(room, botx, boty, botz)
    mapper.update_map(xpt, ypt, zpt)

roommap = mapper.get_map()
x, y, z = roommap.nonzero()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, zdir='z', c='b')
plt.show()
