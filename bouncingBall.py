#Pedro Gallino
#10/25/17
#bouncingBall.py - displays a bouncing ball

from ggame import *

diameter = 50

def moveBall():
    ball.x = ball.x +data['xd']
    ball.y = ball.y +data['yd']

def moveX():
    data['xd'] = -1*(data['xd'])
    
def movey():    
    data['yd'] = -1*(data['yd'])


def step():
    if ball.x+50 > 1024: 
        changex()
    if ball.y+50 > 523:
        changey()
    else:
        moveBall()

    
red = Color(0xFF00, 1)

circle = CircleAsset(diameter,LineStyle(0,red),red)

ball = Sprite(circle,(50,50))

data = {}
data["xd"] = 5.23
data['yd'] = 5.23

App().run(step)

