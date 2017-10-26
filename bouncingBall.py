#Pedro Gallino
#10/25/17
#bouncingBall.py - displays a bouncing ball

from ggame import *

diameter = 50

def moveBall():
    ball.x = ball.x +1
    ball.y = ball.y + 1

def bounceBall():
    ball.x = ball.x - 1
    ball.y = ball.y - 1


def step():
    if ball.x+50 > 1024 or ball.y+50 > 523:
        bounceBall()
    else:
        moveBall()
    


    
red = Color(0xFF00, 1)

circle = CircleAsset(diameter,LineStyle(0,red),red)

ball = Sprite(circle,(50,50))

App().run(step)

