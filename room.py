import numpy as np

class Room (object):

    def __init__(self):
        self.roomsize = 100
        self.room_basic = np.zeros((self.roomsize, self.roomsize, self.roomsize))  # unit is cm, minimum block size is 1cm3
        self.room_basic[70:100, 80:85, 0:22] = 1
        self.room_basic[10:15, 0:30, 0:20] = 1
        self.room_basic[70:90, 0:30, 0:25] = 1
        self.room_basic[8:13, 70:100, 0:25] = 1
        self.room_basic[50:68, 70:75, 0:22] = 1

    def get_room(self):
        return self.room_basic

    def intersection(self, x, y, z):
        if self.room_basic[min(x, self.roomsize - 1), min(y, self.roomsize - 1), min(z, self.roomsize - 1)] == 1:
            return True
        else:
            return False

