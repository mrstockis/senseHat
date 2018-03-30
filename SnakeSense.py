
from time import sleep
from sense_hat import SenseHat
from random import randint

sense = SenseHat()

Li =[100,0,100]
R = [100,0,0]
G = [0,100,0]
B = [0,0,100]
blank = [0,0,0]


def Paint(things):
    sheet = [ blank for i in range(64) ]
    for y in things:
        for i in y:
            y = i[0]+(i[1]*8)
            sheet[y] = i[2]
    return sheet

def Vector(headX,headY,ang):
    if ang == "right":
        if headX < 7: headX += 1
        else: headX += -7
    elif ang == "left":
        if headX > 0: headX += -1
        else: headX += 7
    elif ang == "up":
        if headY > 0: headY += -1
        else: headY += 7
    elif ang == "down":
        if headY < 7: headY += 1
        else: headY += -7
    return headX,headY

def gameLoop():
    score = 0
    x,y = 4,3
    angle = "right"
    snake = [         [3,3,B] , [x,y,B] ]   # [2,3,B] 
    apple = [[randint(0,7),randint(0,7),Li]]

    try:
        while True:
            
            event = sense.stick.get_events()
 #           print(event)
            if len(event):
                if event[0][1] != "middle":
                    angle = event[0][1]
            vect = Vector(x,y,angle)
            x,y = vect[0],vect[1]
            
            for i in snake:
                if i[0] == x and i[1] == y:
                    if score == 0:
                        sense.show_message("Bye!",text_colour=B)
                        sleep(2)
                        sense.clear(); quit()
                    sense.show_message("Score: {}".format(score),text_colour=B)
                    sleep(4)
                    gameLoop()
            
            snake.append([x,y,B]) 
            
            if x == apple[0][0] and y == apple[0][1]:
                apple = [[randint(0,7),randint(0,7),Li]]
                score += 1
            else: snake.pop(0)
            
            sense.set_pixels(Paint([apple,snake]))
#            print("VectorValue:",vect)
 #           print("SnakeList:",snake)
  #          print("ApplePos:",apple)
            sleep(0.3)
    except: KeyboardInterrupt
    sense.clear()
    quit()

gameLoop()

sense.clear()
quit()
