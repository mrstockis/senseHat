
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

G = [0,100,0]
ZZ = [0,0,0]

def MyBin(q):  # expects string
    Len = len(q)
    Str,Base = "",[ 8,4,2,1 ]
    for x,v in enumerate(q):
        Bin,Dig = [],int(v)
        for y,w in enumerate(Base):
            if w <= Dig:
                X = 7-(Len-x)
                Y = 3+y
                Bin.append([X,Y,G]
                Dig -= w
            else Bin += "0"
        Str = Comp + Bin
    for i in 
    return  # [ [x,y,col] , [x,y,col] ]

# for i in 0→64, multiply i with the bin-list to get x,y ??

    
def Paint(things): # a thing is a list of lists of x,y,col
    sheet = [ ZZ for i in range(64) ]
    for y in things:
        for i in y:
            y = i[0]+(i[1]*8)
            sheet[y] = i[2]
    return sheet

Paint(MyBin("123"))

sense.clear()
quit()

