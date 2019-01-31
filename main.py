from lidar import *
from room import room_init
from fake_localization import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

localization = FakeLocalization(50, 50, 50) # starting position in x,y,z

botx, boty, botz = localization.get_curr_estimate()
xpt, ypt, zpt = sense(botx, boty, botz)
room = room_init()
x, y, z = room.nonzero()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for num, i in enumerate(xpt):
    print(xpt[num], ypt[num], zpt[num])
ax.scatter(xpt, ypt, zpt, zdir='z', c='b')
plt.show()
