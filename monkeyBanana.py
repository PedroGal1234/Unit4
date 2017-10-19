#Pedro Gallino
#10/19/17
#monkeyBanana.py - best game ever

from ggame import *
from random import randint
#constants
ROWS = 26
COLS = 50
CELL_SIZE = 20

def moveRight(event):
    if monkey.x < (COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

def moveLeft(event):
    if monkey.x > 0:
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

def moveDown(event):
    if monkey.y < (ROWS-1)*CELL_SIZE:
        monkey.y += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

def moveBanana():
    banana.x = randint(1,COLS-1)*CELL_SIZE
    banana.y = randint(1,ROWS-1)*CELL_SIZE

    
def updateScore():
    data['score'] += 10
    data['scoreText'].destroy()
    scoreBox = TextAsset('Score = '+str(data['score'])) 
    data['scoreText'] = Sprite(scoreBox,(0,(ROWS-2)*CELL_SIZE))

if __name__ == '__main__':
    
    data = {}
    data['score'] = 0
    
    green = Color(0x006600,1)
    brown = Color(0x8b4513,1)
    yellow = Color(0xffff00,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    scoreBox = TextAsset('Score = 0')
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox,((COLS*CELL_SIZE)/2,(ROWS*CELL_SIZE)/2))
    data['scoreText'] = Sprite(scoreBox,(0,(ROWS-2)*CELL_SIZE))
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().run()
