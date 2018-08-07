
    # The Snake game, for senseHat

from time import sleep
from sense_hat import SenseHat
from random import randint,choice
from itertools import cycle

sense = SenseHat()

R = [200,0,50]
G = [0,100,0]
B = [0,0,200]
ZZ = [0,0,0]
Cy =[0,150,190]
Li =[200,0,200]
Ye =[190,150,0]
Or =[200,100,0]
Tu =[0,100,50]
Ne = [100,10,50]

Mix = [R]
stripe1 = cycle([Ye,Or])
stripe2 = cycle([B,Cy])
stripe3 = cycle([G,Tu])

gameTime = 0.35
    
def Paint(things): # thing is a list of lists of x,y,col
    picture = [ ZZ for i in range(64) ] # blank page
    for thing in things:
        for i in thing:
            y = i[0]+(i[1]*8)
            picture[y] = i[2]
    return picture

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
    time = 0
    x,y = 4,3
    angle = "right"
    snake = [ [2,3,G], [3,3,Tu] , [x,y,G] ]
    apple = [[randint(0,7),randint(0,7),choice(Mix)]]

    try:
        while True:
            
            event = sense.stick.get_events()
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

                    score = int(((score**2)/time)*100)
                    sense.show_message("Score  {}".format(score),text_colour=B)
                    sleep(4)
                    gameLoop()
            
            snake.append([x,y,next(stripe3)]) 
            
            if x == apple[0][0] and y == apple[0][1]:
                apple = [[randint(0,7),randint(0,7),choice(Mix)]]
                score += 1
            else: snake.pop(0)
            
            sense.set_pixels(Paint([apple,snake]))
            time += gameTime
            sleep(gameTime)


    except: KeyboardInterrupt

    sense.clear()
    quit()

gameLoop()

sense.clear()
quit()

# salvage

GG = [0,100,0]
RR = [100,0,0]
YY = [100,100,0]
Ne = [100,10,50]
Cy = [30,100,100]
BB = [20,10,100]
ZZ = [0,0,0]

try:
    while True:
        inp = int(input("Paint nr: "))
        C = Ne
        a = inp

# Skapar strängen som sen blir bilden; glömt
        img=""; revNr=str(abs(a))[::-1]
# Trimma binär affix, tror jag
        for i in revNr:
            binary=bin(int(i))[2::]

# Fyll rader med binära längd + kompletterande 0'or
            comp=8-len(binary)
            row="0"*comp+binary
            img+=row

# Fyll och gör till Lista
        img = img+(64-len(img))*"0"
        img = list(img)

# Rotera90 1: matris (lista med listor), 2: reversera matrisen, 3: läs av columnvis, 4: "plana ut" listorna till en enda
        img = [img[i:i+8] for i in range(0,len(img),8)]
        img = img[::-1]
        img = zip(*img)
        img = [z for i in img for y in i for z in y]

# Ersätt alla tecken med Variabler { 1: G/R, 0: Z }
        for n,i in enumerate(img):
            if i=="1": img[n]=C
            else: img[n]=ZZ

        sense.set_pixels(img)
        #zZz(1)

except KeyboardInterrupt:

    sense.clear()
    exit
