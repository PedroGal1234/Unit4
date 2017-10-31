#Pedro Gallino
#10/27/17
#pong - the pong game


from ggame import *

radius = 12.5

def moveBall():
    if data["ball"].x+radius >= 1015:
        updateScore1()
        stop()
    if data["ball"].x-radius <= 0:
        updateScore2()
        stop
    data["ball"].x = data["ball"].x +1.5*data['xd']
    data["ball"].y = data["ball"].y +1.5*data['yd']

def moveX():
    data['xd'] = -1*(data['xd'])
    
def moveY():    
    data['yd'] = -1*(data['yd'])

def moveUp1(event):
    data["paddle1"].y = data["paddle1"].y-40
def moveDown1(event):
        data["paddle1"].y = data["paddle1"].y+40
def moveUp2(event):
    data["paddle2"].y = data["paddle2"].y-40
def moveDown2(event):
        data["paddle2"].y = data["paddle2"].y+40

def step():
    if data["ball"].x-radius <= 25 and data['ball'].y >= data["paddle1"].y and data["ball"].y <= (data["paddle1"].y+200): 
        moveX()
    if data["ball"].x+radius >= 985 and data["ball"].y >= data["paddle2"].y and data["ball"].y <= (data["paddle2"].y+200):
        moveX()
    if data["ball"].y+radius >= 523 or data["ball"].y-radius <= 0:
        moveY()
    moveBall()


def updateScore1():
    data["score1"] += 1

def updateScore2():
    data["score2"] += 1
    
def reset(event):
    data["ball"].destroy()
    data["paddle1"].destroy()
    data["paddle2"].destroy()
    
    data["scoreText1"].destroy()
    scoreBox1 = TextAsset("Left: "+str(data["score1"]))
    data["scoreText2"].destroy()
    scoreBox2 = TextAsset("Right: "+str(data["score2"]))
    
    circle = CircleAsset(radius,LineStyle(0,red),red)
    rectangle1 = RectangleAsset(25,200,LineStyle(1, blue), blue)
    rectangle2 = RectangleAsset(25,200,LineStyle(1, blue), blue)
    
    data["scoreText1"] = Sprite(scoreBox1, (450,0))
    data["scoreText2"] = Sprite(scoreBox2, (450,25))
    
    data["ball"] = Sprite(circle,(500,500))
    data["paddle1"] = Sprite(rectangle1,(0,200))
    data["paddle2"] = Sprite(rectangle2,(985,200))
    
    App().run(step)

if __name__ == "__main__":    
    
    red = Color(0xFF0000, 1)
    blue = Color(0x0000ff,1)
    green = Color(0x00ff00,1)
    circle = CircleAsset(radius,LineStyle(0,red),red)
    rectangle1 = RectangleAsset(25,200,LineStyle(1, blue), blue)
    rectangle2 = RectangleAsset(25,200,LineStyle(1, blue), blue)
    
    data = {}

    data["ball"] = Sprite(circle,(500,500))
    data["paddle1"] = Sprite(rectangle1,(0,200))
    data["paddle2"] = Sprite(rectangle2,(985,200))
    
    scoreBox1 = TextAsset("Left: 0")
    scoreBox2 = TextAsset("Right: 0")
    data["scoreText1"] = Sprite(scoreBox1, (450,0))
    data["scoreText2"] = Sprite(scoreBox2, (450,25))
    data["score1"] = 0
    data["score2"] = 0
    
    data["xd"] = 5
    data['yd'] = 5
    
    
    App().listenKeyEvent("keydown","w", moveUp1)
    App().listenKeyEvent("keydown","s", moveDown1)
    App().listenKeyEvent("keydown","up arrow", moveUp2)
    App().listenKeyEvent("keydown","down arrow", moveDown2)
    App().listenKeyEvent("keydown","space", reset)
    App().run(step)


