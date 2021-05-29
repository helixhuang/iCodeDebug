from Util import Log

class DevClass:
    x = 0
    y = 0
    d = 0
    energy = 100

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
    
    def step(self,n):
        Log.info(n, f'Dev.step({n})')

    def wait(self):
        Log.info(0, f'Dev.wait()')

    def turnLeft(self):
        Log.info(1, f'Dev.turnLeft()')

    def turnRight(self):
        Log.info(1, f'Dev.turnRight()')
