from lidar import *
from room import *
from fake_localization import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

localization = FakeLocalization(50, 50, 10) # starting position in x,y,z

botx, boty, botz = localization.get_curr_estimate()
room = Room()
lidar = Lidar()
xpt, ypt, zpt = lidar.sense(room, botx, boty, botz)
room_init = room.get_room()
x, y, z = room_init.nonzero()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xpt, ypt, zpt, zdir='z', c='b')
plt.show()
