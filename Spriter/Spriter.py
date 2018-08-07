# Create, add, change, and play through sprites to animate

# Upper right, Pallete; up/down:light, left/right:color
# Upper left, save active sprite to list
# Right bottom, Play: up/down speed, Right:play, Left:pause/load sprite

# save seperate animations/siries of sprites, so that one can animate different things seperately
# then when animating all of them, loop the range of the longest, and have the others pre-repeat, by modulus of each their lengths
# paralell animations, of different length, dynamically adjust, by unique modulus of index by lengthiest animation

# things[n_saved[n_sprites]]; for frame in range(bigThing): paint([thing[frame % len(thing)] for thing in things])

from sense_hat import SenseHat; sense = SenseHat()
from itertools import cycle
from time import sleep
from random import randint

sense.clear()
#quit()

R  = [100,0,0]
RG = [100,100,0]
G  = [0,100,0]
GB = [0,100,100]
B  = [0,0,100]
BR = [100,0,100]

blank, grey = [0,0,0], [50,50,50]
colors = cycle([ R,RG,G,GB,B,BR, blank])

spriteDest = "sprites/"
cursor = [ [27, grey  ] ]
buttons = [[0,grey],[7,grey],[56,grey],[63,grey]]



def T(thing,comment=""):
    print(comment+"\n",thing)


#---
def pallette(rgbC, direction):  # rgbCurrent
    s = 10  # step
    
    #default to red, returning from blank/eraser
    if not sum(rgbC): rgbC = R  

    # transform to suite logic / removes lighting modification
    m = min(rgbC)
    plt = [ i-m for i in rgbC ]

    # addative pallette, shift light and color
    if direction == "left" or direction == "right":
        if sum([ abs(i) for i in plt[0:2] ]) == 100:
            plt[ 1 if direction == "left" else 0 ] -= s
            plt[ 0 if direction == "left" else 1 ] += s            
        if sum([ abs(i) for i in plt[1:3] ]) == 100:
            plt[ 2 if direction == "left" else 1 ] -= s
            plt[ 1 if direction == "left" else 2 ] += s
        if sum([ abs(i) for i in plt[0:3:2] ]) == 100:
            plt[ 0 if direction == "left" else 2 ] -= s
            plt[ 2 if direction == "left" else 0 ] += s

    elif direction == "up" and max(rgbC) + max(plt) <= 250-s:
        for i in range(3):
            plt[i] += s
        
    elif direction == "down" and min(rgbC) + min(plt) >= s:
        for i in range(3):
            plt[i] -= s
        
    # mash / add pallete to rgbC within restrictions
    newColor = [ (m + plt[i]) % 200 for i in range(3) ]

    return newColor


def load(index,rate):
    x = index % 8
    y = int(index / 8)
    groups = [[0,1],[1,2],[2,0]]
    rgb = [0,0,0]
    for c in range(10):
        for g in groups:
            for v in range(0,200,10*(c+1)):
                rgb[g[0]], rgb[g[1]] = 240-v, 40+v
                sense.set_pixel(x,y,rgb)
                sleep(rate)


# each thing is a list of diods, where diods are 2 element lists of position and color-list
# thing: [ diod1, diod2, ... ]; where diod: [ position, [color] ]
def paint(things):
    canvas = [ blank for i in range(64) ]
    for thing in things:
        for diod in thing:  # diod: [index,[color]]
            canvas[diod[0]] = diod[1]
    sense.set_pixels(canvas)


def catchStick(state):
    event = sense.stick.get_events()
    if len(event) and event[0][2] == state:
        return event[0][1]
    return False


def pickColor(currentColor):
    changed = False
    while True:
        event = catchStick("pressed")
        if event:
            if event == "middle":
                if not changed: return blank
                else: return currentColor
            else:
                changed = True
                currentColor = pallette(currentColor,event)
                sense.set_pixel(7,0,currentColor)
        #
        sleep(1/20)


def move(direction,cursor):
    if direction == "up": return -8 if cursor > 7 else 56
    elif direction == "down": return 8 if cursor < 56 else -56
    elif direction == "left": return -1 if cursor % 8 else 7
    elif direction == "right": return 1 if (cursor+1) % 8 else -7


def animate(thingys):
    c = 0
    sizes = [ len(thing) for thing in thingys ]
    rate = 0.5
    print(len(thingys))
    T( [  len(thing) for thing in thingys ], "len(thing)")
    #
    while True:
        if catchStick("pressed"): return
        #
        paint( [ thing[ c % sizes[i] ] for i,thing in enumerate(thingys) ] )
        #
        c += 1
        sleep(rate)


def export(work):
    # get more unique ID by taking the sum of all colors prefixed by number of sprites
    colorSum = 0
    for a in work: # each animation
        for s in a: # each sprite
            for d in s: # each diode
                for c in d[1]: # each colorvalue in colorlist
                    colorSum += c
#    colorSum = sum ( [ c for c in d[1] for d in s for s in work ] )
    colorSum = str(colorSum)
    animeCount = str( len( work ) )
    filename = "sprite_"+animeCount+"_"+colorSum
    #
    f = open(spriteDest+filename,"w")
    f.write(str(work))
    f.close()
    
    T(spriteDest+filename,"saved")


def main():
    #
    sprite = [ [ i, blank ] for i in range(64) ]
    saved = []
    things = []
    paint([sprite,buttons,cursor])
    activeColor = blank
    changed = True
    #
    while True:
        event = catchStick("pressed")
        if event:
            if event != "middle": cursor[0][0] += move(event,cursor[0][0])
            else:
                if cursor[0][0] == 7:
                    activeColor = pickColor(activeColor)
                    buttons[1][1] = activeColor
                #
                elif cursor[0][0] == 0:
                    if not changed:
                        things.append( [ [ [p for p in d ] for d in s if sum(d[1]) ] for s in saved ] )  # try to remake the thing
                        saved , sprite = [] , [ [ i, blank ] for i in range(64) ]  # nullify
                        load(0,0.01)
                    else: saved.append([ [piece for piece in diod] for diod in sprite]); load(0,0.001)
                    changed = False
                #
                elif cursor[0][0] == 56: print(things); export(things); load(56,0.001)
                #
                elif cursor[0][0] == 63:
                    load(63,0.001)
                    if saved == []: animate(things)
                    else: animate([saved])
                #
                else: sprite[cursor[0][0]][1] = activeColor; changed = True
            #
            paint([sprite,buttons,cursor])
        #
        sleep(1/20)
#'''


#try:
#    main()
#except: KeyboardInterrupt

main()
sense.clear()

