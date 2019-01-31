import numpy as np

class Mapping(object):
    def __init__(self):
        self.map = np.zeros((100, 100, 100))

    def update_map(self, xpt, ypt, zpt):
        for num, j in enumerate(xpt):
            self.occupy_cell(xpt[num], ypt[num], zpt[num])

    def get_map(self):
        return self.map

    def occupy_cell(self, xpt, ypt, zpt):
        self.map[min(int(xpt), 99), min(int(ypt), 99), min(int(zpt), 99)] = 1

