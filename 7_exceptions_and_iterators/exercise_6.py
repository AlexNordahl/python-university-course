import itertools
import random

class ZeroOne:
    def __init__(self):
        self.flag = False

    def __call__(self):
        if self.flag == False:
            self.flag = True
            return 0
        
        self.flag = False
        return 1

class RandomDir:
    def __init__(self):
        self.dirs = ['N', 'E', 'S', 'W']

    def __call__(self):
        return self.dirs[random.randint(0, len(self.dirs) - 1)]

class NextDay():
    def __init__(self):
        self.days = [0, 1, 2, 3, 4, 5, 6]
        self.cur = -1
    
    def __call__(self):
        self.cur += 1

        if self.cur == len(self.days):
            self.cur = 0

        return self.days[self.cur]