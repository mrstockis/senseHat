from random import randint as rand
from sense_hat import SenseHat
from time import sleep
from itertools import cycle
sense = SenseHat()
#sense.flipH()
#sense.flipV()

I,O = [250,250,250],[000,000,000]   # White,Black
r = [100,000,000]   # Red
R = [50,000,000]    # Red dark
g = [000,100,000]   # Green
G = [000,50,000]    # Green dark
b = [000,000,100]   # Blue
B = [000,000,50]    # Blue dark
y = [100,100,0]     # Yellow
o = [150,50,0]      # Orange
i = [100,50,0]      # OrangeDark(blink)
p = [150,50,50]     # Pink
t = [0,75,100]      # Turquoise
T = [0,70,110]      # Teal
s = [50,55,60]      # Sky



dudeNorm = [
        O,O,y,y,y,y,O,O,
        O,O,t,o,t,o,y,O,
        O,O,o,o,o,o,y,O,
        O,O,O,O,o,O,O,O,
        O,O,b,b,o,b,O,O,
        O,b,O,b,b,b,b,O,
        O,R,O,B,B,B,O,b,
        G,R,G,r,G,r,G,G,
        ]

dudeBlink = [
        O,O,y,y,y,y,O,O,
        O,O,i,o,i,o,y,O,
        O,O,o,o,o,o,y,O,
        O,O,O,O,o,O,O,O,
        O,O,b,b,o,b,O,O,
        O,b,O,b,b,b,b,O,
        O,R,O,B,B,B,O,b,
        G,R,G,r,G,r,G,G,
        ]

dudeBack = [
        O,O,O,y,y,y,y,O,
        O,O,O,t,o,t,o,y,
        O,O,O,o,o,o,o,y,
        O,O,O,O,O,o,O,O,
        O,O,b,b,o,b,O,O,
        O,b,O,b,b,b,b,O,
        O,R,O,B,B,B,O,b,
        G,R,G,r,G,r,G,G,
        ]

dudeForw = [
        O,y,y,y,y,O,O,O,
        O,t,o,t,o,y,O,O,
        O,o,o,o,o,y,O,O,
        O,O,O,o,O,O,O,O,
        O,O,b,b,o,b,O,O,
        O,b,O,b,b,b,b,O,
        O,R,O,B,B,B,O,b,
        G,R,G,r,G,r,G,G,
        ]

dude = [
            [dudeNorm,1],
            [dudeForw,1],
            [dudeNorm,1],
            [dudeBlink,0.5]
            ]
dude = cycle(dude)

try:
    for i in dude:
        sense.set_pixels(i[0])
        sleep(i[1])
except: KeyboardInterrupt


'''
for y in range(255):
    gnu=[]
    for i in range(1,65):
        gnu+=[[(200-i*3),y,y]]
    sleep(0.001)
    sense.set_pixels(gnu)
sleep(5)
'''

'''
g=rand(0,10)
print(g)
for i in range(100):
#while True:
    x=rand(0,7)
    y=rand(0,7)
    sense.set_pixel(x,y,[(x**y)%255,(y**x)%255,(i**i)%255])
    sleep(0.1)
sleep(5)
'''

'''
y=0
for i in range(64):
    sense.set_pixel(i%8,y,[(i*2)%255,(i*3)%255,(i*4)%255])
    if i%8==0:
        y+=1
    sleep(0.1)
'''

#RGB = [0,0,0]
#for i in [[r,g],[g,b],[b,r]]:
#    for y in range(0,255):
#        RGB


try:
    while True:
        color = [ int(i) for i in input("RGB: ").split(" ") ]
        img = [ color for i in range(64) ]
        sense.set_pixels(img)

except: KeyboardInterrupt


#Updates 64 element list (entire led matrix)
#sense.set_pixels(img)
#sleep(5)
sense.clear()
