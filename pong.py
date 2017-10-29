#Pedro Gallino
#10/27/17
#pong - the pong game


from ggame import *

radius = 25

def moveBall():
    if ball.x+25 >= 1015:
        updateScore1()
    if ball.x<= 0:
        updateScore1()
    ball.x = ball.x +data['xd']
    ball.y = ball.y +data['yd']

def moveX():
    data['xd'] = -1*(data['xd'])
    
def moveY():    
    data['yd'] = -1*(data['yd'])

def moveUp1(event):
    if paddle1.y > 0:
        paddle1.y = paddle1.y-20
def moveDown1(event):
        paddle1.y = paddle1.y+20
def moveUp2(event):
    if paddle2.y > 0:    
        paddle2.y = paddle2.y-20
def moveDown2(event):
        paddle2.y = paddle2.y+20

def step():
    if ball.x-25 <= 50 and ball.y >= paddle1.y and ball.y <= (paddle1.y+200): 
        moveX()
    if ball.x+25 >= 960 and ball.y >= paddle2.y and ball.y <= (paddle2.y+200):
        moveX()
    if ball.y+25 >= 523 or ball.y-25 <= 0:
        moveY()
    moveBall()

def updateScore1():
    reset()
    data["score1"] += 1
    data["scoreText1"].destroy()
    scoreBox1 = TextAsset("Player1: "+str(data["score"]))
    data["scoreText1"] = Sprite(scoreBox1,(450,0))
    reset()

def updateScore2():
    reset()
    data["score2"] += 1
    data["scoreText2"].destroy()
    scoreBox2 = TextAsset("Player2: "+str(data["score"]))
    data["scoreText2"] = Sprite(scoreBox2,(450,25))

def reset():
    ball.destroy()
    paddle1.destroy()
    paddle2.destroy()
    circle = CircleAsset(radius,LineStyle(0,red),red)
    rectangle1 = RectangleAsset(50,200,LineStyle(1, blue), blue)
    rectangle2 = RectangleAsset(50,200,LineStyle(1, blue), blue)
    ball = Sprite(circle,(300,300))
    paddle1 = Sprite(rectangle1,(0,200))
    paddle2 = Sprite(rectangle2,(960,200))
    App().run(step)

if __name__ == "__main__":    
    
    red = Color(0xFF0000, 1)
    blue = Color(0x0000ff,1)
    green = Color(0x00ff00,1)
    circle = CircleAsset(radius,LineStyle(0,red),red)
    rectangle1 = RectangleAsset(50,200,LineStyle(1, blue), blue)
    rectangle2 = RectangleAsset(50,200,LineStyle(1, blue), blue)
    scoreBox1 = TextAsset("Player1: 0")
    scoreBox2 = TextAsset("Player2: 0")
    
    data = {}
    data["scoreText1"] = Sprite(scoreBox1,(450,0))
    data["scoreText2"] = Sprite(scoreBox2,(450,25))
    ball = Sprite(circle,(300,300))
    paddle1 = Sprite(rectangle1,(0,200))
    paddle2 = Sprite(rectangle2,(960,200))
    
    data["score1"] = 0
    data["score2"] = 0
    data["xd"] = 10
    data['yd'] = 10
    App().listenKeyEvent("keydown","w", moveUp1)
    App().listenKeyEvent("keydown","s", moveDown1)
    App().listenKeyEvent("keydown","up arrow", moveUp2)
    App().listenKeyEvent("keydown","down arrow", moveDown2) 
    App().run(step)


