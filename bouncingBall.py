#Pedro Gallino
#10/25/17
#bouncingBall.py - displays a bouncing ball

from ggame import *

radius = 50

def moveBall():
    ball.x = ball.x -data['xd']
    ball.y = ball.y +data['yd']

def moveX():
    data['xd'] = -1*(data['xd'])
    
def movey():    
    data['yd'] = -1*(data['yd'])


def step():
    if ball.x+50 >= 1015 or ball.x-50 <= 0: 
        movex()
    if ball.y+50 >= 523 or ball.y-50 <= 0:
        movey()
    moveBall()

if __name__ == "__main__":    
    red = Color(0xFF00, 1)
    
    circle = CircleAsset(radius,LineStyle(0,red),red)
    
    ball = Sprite(circle,(100,100))
    
    data = {}
    data["xd"] = 5.23
    data['yd'] = 5.23
    
    App().run(step)

