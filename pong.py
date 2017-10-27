#Pedro Gallino
#10/27/17
#pong - the pong game

#Pedro Gallino
#10/25/17
#bouncingBall.py - displays a bouncing ball

from ggame import *

radius = 50

def moveBall():
    ball.x = ball.x +data['xd']
    ball.y = ball.y +data['yd']

def moveX():
    data['xd'] = -1*(data['xd'])
    
def moveY():    
    data['yd'] = -1*(data['yd'])

def moveUp1(event):
    paddle1.y = paddle1.y-10
def moveDown1(event):
    paddle1.y = paddle1.y+10
def moveUp2(event):
    paddle2.y = paddle2.y-10
def moveDown2(event):
    paddle2.y = paddle2.y+10

def step():
    if ball.x+50 >= 1015 or ball.x-50 <= 0: 
        moveX()
    if ball.y+50 >= 523 or ball.y-50 <= 0:
        moveY()
    moveBall()

if __name__ == "__main__":    
    red = Color(0xFF0000, 1)
    blue = Color(0x0000ff,1)
    green = Color(0x00ff00,1)
    circle = CircleAsset(radius,LineStyle(0,red),red)
    rectangle1 = RectangleAsset(50,200,LineStyle(1, blue), blue)
    rectangle2 = RectangleAsset(50,200,LineStyle(1, blue), blue)
    
    
    ball = Sprite(circle,(51,51))
    paddle1 = Sprite(rectangle1,(0,200))
    paddle2 = Sprite(rectangle2,(965,200))
    
    
    data = {}
    data["xd"] = 10
    data['yd'] = 10
    App().listenKeyEvent("keydown","w", moveUp1)
    App().listenKeyEvent("keydown","s", moveDown1)
    App().listenKeyEvent("keydown","up arrow", moveUp2)
    App().listenKeyEvent("keydown","down arrow", moveDown2) 
    App().run(step)

