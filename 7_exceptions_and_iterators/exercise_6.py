import random

class ZeroOne:
    def __init__(self):
        self.flag = True

    def __iter__(self):
        return self

    def __next__(self):
        self.flag = not self.flag
        return int(self.flag)
    
zo = ZeroOne()
assert(next(zo) == 0)
assert(next(zo) == 1)
assert(next(zo) == 0)

class RandomDir:
    def __init__(self):
        self.dirs = ['N', 'E', 'S', 'W']

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.dirs)

class NextDay():
    def __init__(self):
        self.days = [0, 1, 2, 3, 4, 5, 6]
        self.cur = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.cur += 1

        if self.cur == len(self.days):
            self.cur = 0

        return self.days[self.cur]