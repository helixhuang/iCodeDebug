
import builtins
from Util import Log

from Model.Dev import DevClass
from Model.Spaceship import SpaceshipClass
from Model.Item import ItemClass
from Model.Flyer import FlyerClass

#################### 此区域用于初始化 ####################
builtins.step = 0

def wait():
    Log.info(0, f'wait()')

Dev = DevClass(0,0,0)
Spaceship = SpaceshipClass(0,0,0)

Flyer = []
for i in range(20):
    Flyer.append(FlyerClass(0,0,0))

Item = []
for i in range(20):
    Item.append(ItemClass(0,0,0))


#########################################################

#################### 此区域用于实际代码 ###################
for i in range(9):
    Dev.step((i==0)+(i==1)*3-(i==2)-(i==3 or i==6 or i==7)*2+(i==4 or i==8)*2-(i==5)*4)
#########################################################
