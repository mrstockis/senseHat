#from subprocess import call
from time import sleep as zZz
from sense_hat import SenseHat

sense = SenseHat()
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
