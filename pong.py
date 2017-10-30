#Pedro Gallino
#10/27/17
#pong - the pong game


from ggame import *

radius = 25

def moveBall():
    if data["ball"].x+radius >= 1015:
        updateScore1()
    if data["ball"].x-radius <= -50:
        updateScore1()
    data["ball"].x = data["ball"].x +data['xd']
    data["ball"].y = data["ball"].y +data['yd']

def moveX():
    print('hello')
    data['xd'] = -1*(data['xd'])
    
def moveY():    
    data['yd'] = -1*(data['yd'])

def moveUp1(event):
    if data["paddle1"].y > 0:
        data["paddle1"].y = data["paddle1"].y-20
def moveDown1(event):
        data["paddle1"].y = data["paddle1"].y+20
def moveUp2(event):
    if data["paddle2"].y > 0:    
        data["paddle2"].y = data["paddle2"].y-20
def moveDown2(event):
        data["paddle2"].y = data["paddle2"].y+20

def step():
    if data["ball"].x-radius <= 50 and ball.y >= data["paddle1"].y and data["ball"].y <= (data["paddle1"].y+200): 
        moveX()
    if data["ball"].x+radius >= 960 and data["ball"].y >= data["paddle2"].y and data["ball"].y <= (data["paddle2"].y+200):
        moveX()
    if data["ball"].y+radius >= 523 or data["ball"].y-radius <= 0:
        moveY()
    moveBall()

def reset(event):
    data["ball"].destroy()
    data["paddle1"].destroy()
    data["paddle2"].destroy()
    
    circle = CircleAsset(radius,LineStyle(0,red),red)
    rectangle1 = RectangleAsset(50,200,LineStyle(1, blue), blue)
    rectangle2 = RectangleAsset(50,200,LineStyle(1, blue), blue)
    
    data["ball"] = Sprite(circle,(500,500))
    data["paddle1"] = Sprite(rectangle1,(0,200))
    data["paddle2"] = Sprite(rectangle2,(960,200))
    App().run(step)

if __name__ == "__main__":    
    
    red = Color(0xFF0000, 1)
    blue = Color(0x0000ff,1)
    green = Color(0x00ff00,1)
    circle = CircleAsset(radius,LineStyle(0,red),red)
    rectangle1 = RectangleAsset(50,200,LineStyle(1, blue), blue)
    rectangle2 = RectangleAsset(50,200,LineStyle(1, blue), blue)
    
    data = {}

    data["ball"] = Sprite(circle,(500,500))
    data["paddle1"] = Sprite(rectangle1,(0,200))
    data["paddle2"] = Sprite(rectangle2,(960,200))
    
    data["xd"] = 5
    data['yd'] = 5
    App().listenKeyEvent("keydown","w", moveUp1)
    App().listenKeyEvent("keydown","s", moveDown1)
    App().listenKeyEvent("keydown","up arrow", moveUp2)
    App().listenKeyEvent("keydown","down arrow", moveDown2)
    App().listenKeyEvent("keydown","space", reset)
    App().run(step)


