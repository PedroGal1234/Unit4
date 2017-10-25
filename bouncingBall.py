#Pedro Gallino
#10/25/17
#bouncingBall.py - displays a bouncing ball

from ggame import *

diameter = 50

def moveBall():
    ball.x = ball.x +1
    ball.y = ball.y + 1
    data['frames'] = 0

def bounceBall():
    ball.x = ball.x - 1
    ball.y = ball.y - 1
    data['frames'] = 0


def step():
    data['frames'] += 1
    if data['frames'] == 1:
        if ball.x+50 == 523 and ball.y+50 == 1012:
            bounceBall()
        else:
            moveBall()
    


data = {}
data['frames'] = 0
    
red = Color(0xFF00, 1)

circle = CircleAsset(diameter,LineStyle(10,red),red)

ball = Sprite(circle,(50,50))

App().run(step)

