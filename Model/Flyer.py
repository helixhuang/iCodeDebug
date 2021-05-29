from Util import Log
import time

class FlyerClass:
    x = 0
    y = 0
    d = 0

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
    
    def disappear(self):
        result = int(time.time() % 60)%2==0
        Log.info(0, f'Flyer.disappear() : {result}')
        return result

    def step(self,n):
        Log.info(n, f'Dev.step({n})')