from Util import Log

class SpaceshipClass:
    x = 0
    y = 0
    d = 0

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def step(self, n):
        Log.info(n, f'Spaceship.step({n})')

    def wait(self):
        Log.info(0, f'Spaceship.wait()')

    def turnLeft(self):
        Log.info(1, f'Spaceship.turnLeft()')

    def turnRight(self):
        Log.info(1, f'Spaceship.turnRight()')