#Pedro Gallino
#10/16/17
#colorChangeWindow.py 

from ggame import *
from random import randint

diameter = randint(1,100)

def mouseClick(event): 
    x = randint(1,400)
    y = randint(1,400)
    diameter = randint(1,100)
    num = randint(1,6)
    if num == 1:
        color = Color(0xff0000,1)
    elif num == 2:
        color = Color(0x000ff,1)
    elif num == 3:
        color = Color(0xffff00,1)
    elif num == 4:
        color = Color(0xff33ff,1)
    elif num == 5:
        color = Color(0x66cc00,1)
    elif num == 6:
        color = Color(0xff8000,1)
    
    line = LineStyle(3,color)
    circle = CircleAsset(diameter,line,color)
    
    Sprite(circle,(x,y))

App().listenMouseEvent('click',mouseClick)
App().run()
