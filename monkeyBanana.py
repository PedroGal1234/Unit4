#Pedro Gallino
#10/19/17
#monkeyBanana.py - best game ever

from ggame import *

#constants
ROWS = 25
COLS = 50
CELL_SIZE = 20

if __name__ == '__main__':
    
    green = Color(0x006600,1)
    brown = Color(0x8b4513,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    
    Sprite(jungleBox)
    Sprite(monkeyBox)
    App().run()
