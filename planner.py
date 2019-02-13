import numpy as np
import math
import copy
import random

class Node():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.parent = None

class Planner(object):
    def __init__(self, goal, start):
        self.goal = goal
        self.expandDis = 1.0
        self.goalSampleRate = 10
        self.maxIter = 500
        self.nodeList = [start]

    def GetNearestListIndex(self, nodeList, rnd):
        dlist = [(node.x - rnd[0]) ** 2 + (node.y - rnd[1])
                 ** 2 for node in nodeList]
        minind = dlist.index(min(dlist))
        return minind

    def iterate_planner(self, map, botx, boty, botz):

        if random.randint(0, 100) > self.goalSampleRate:
            rnd = [random.uniform(0, 100), random.uniform(0, 100)]
        else:
            rnd = [self.goal.x, self.goal.y]

        nind = self.GetNearestListIndex(self.nodeList, rnd)

        nearestNode = self.nodeList[nind]
        theta = math.atan2(rnd[1] - nearestNode.y, rnd[0] - nearestNode.x)

        newNode = copy.deepcopy(nearestNode)
        newNode.x += self.expandDis * math.cos(theta)
        newNode.y += self.expandDis * math.sin(theta)
        newNode.z = botz
        # newNode.parent = nind

        self.nodeList.append(newNode)

        newx = newNode.x
        newy = newNode.y
        newz= botz

        if map[int(newx), int(newy), int(newz)] == 1:
            return botx, boty, botz

        # check goal
        dx = newNode.x - self.goal.x
        dy = newNode.y - self.goal.y
        d = math.sqrt(dx * dx + dy * dy)
        if d <= self.expandDis:
            print("Goal!!")
            return

        return newx, newy, newz





