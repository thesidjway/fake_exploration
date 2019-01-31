import numpy as np

def room_init():
    room_basic = np.zeros((100, 100, 100))  # unit is cm, minimum block size is 1cm3
    room_basic[70:100, 80:85, 0:22] = 1
    room_basic[10:15, 0:30, 0:20] = 1
    room_basic[70:90, 0:30, 0:25] = 1
    room_basic[8:13, 70:100, 0:25] = 1
    room_basic[50:68, 70:75, 0:22] = 1
    return room_basic


