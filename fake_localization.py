import numpy as np


class FakeLocalization(object):

    def __init__(self, x, y, z):
        self.curr_x = x
        self.curr_y = y
        self.curr_z = z

    def get_curr_estimate(self):
        return self.curr_x, self.curr_y, self.curr_z

    def update_position(self, new_x, new_y, new_z):
        self.curr_x = new_x
        self.curr_y = new_y
        self.curr_z = new_z
