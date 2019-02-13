import sys
from lidar import *
from room import *
from mapping import *
from planner import *
from fake_localization import *
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

localization = FakeLocalization(50, 50, 10)  # starting position in x,y,z
room = Room()
lidar = Lidar()
mapper = Mapping()
goal = Node(75, 25, 10)
start = Node(50, 50, 10)
planner = Planner(goal, start)

fig = plt.figure()
ax = fig.add_subplot(111,  projection='3d')
save_animation = False


def update_plot(i):
    roommap = mapper.get_map()
    botx, boty, botz = localization.get_curr_estimate()
    newx, newy, newz = planner.iterate_planner(roommap, botx, boty, botz)
    localization.update_position(newx, newy, newz)
    botx, boty, botz = localization.get_curr_estimate()
    xpt, ypt, zpt = lidar.sense(room, botx, boty, botz)
    mapper.update_map(xpt, ypt, zpt)
    roommap = mapper.get_map()
    x, y, z = roommap.nonzero()
    ax.clear()
    ax.scatter(x, y, z, zdir='z', c='b')
    ax.scatter(botx, boty, botz, zdir='z', c='r')


ani = animation.FuncAnimation(fig, update_plot, frames=np.arange(0, 50), interval=200)
if len(sys.argv) > 1 and sys.argv[1] == 'save':
    ani.save('animation.gif', dpi=80, writer='imagemagick')
else:
    plt.show()
