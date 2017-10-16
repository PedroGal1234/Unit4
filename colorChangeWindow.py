#Pedro Gallino
#10/16/17
#colorChangeWindow.py 

from ggame import *
from random import randint

def mouseClick(event):    
    num = randint(1,6)
    if num == 1:
        red = Color(0xff0000,1)
        line = LineStyle(3,red)
        rectangle = RectangleAsset(1000,1000,line,red)
    elif num == 2:
        blue = Color(0x000ff,1)
        line = LineStyle(3,blue)
        rectangle = RectangleAsset(1000,1000,line,blue)
    elif num == 3:
        yellow = Color(0xffff00,1)
        line = LineStyle(3,yellow)
        rectangle = RectangleAsset(1000,1000,line,yellow)
    elif num == 4:
        purpel = Color(0xff33ff,1)
        line = LineStyle(3,purpel)
        rectangle = RectangleAsset(1000,1000,line,purpel)
    elif num == 5:
        green = Color(0x66cc00,1)
        line = LineStyle(3,green)
        rectangle = RectangleAsset(1000,1000,line,green)
    elif num == 6:
        orange = Color(0xff8000,1)
        line = LineStyle(3,orange)
        rectangle = RectangleAsset(1000,1000,line,orange)
    
    Sprite(rectangle)

App().listenMouseEvent('click',mouseClick)
App().run()

