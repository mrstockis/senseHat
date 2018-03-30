from subprocess import call 
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request
from time import sleep as zZz
from sense_hat import SenseHat
from itertools import cycle

sense = SenseHat()
GG = [0,100,0]
RR = [100,0,0]
YY = [100,100,0]
Ne = [100,10,50]
Cy = [30,100,100]
BB = [20,10,100]
ZZ = [0,0,0]
Gr = [50,50,50]
mode = cycle([1,2,3,4])

try:
    while True:
# En bild medans datan laddas
        BC = [
                ZZ,ZZ,YY,ZZ,YY,ZZ,ZZ,ZZ,
                ZZ,YY,YY,YY,YY,ZZ,ZZ,ZZ,
                ZZ,ZZ,YY,ZZ,ZZ,YY,ZZ,ZZ,
                ZZ,ZZ,YY,YY,YY,ZZ,ZZ,ZZ,
                ZZ,ZZ,YY,ZZ,ZZ,YY,ZZ,ZZ,
                ZZ,ZZ,YY,ZZ,ZZ,YY,ZZ,ZZ,
                ZZ,YY,YY,YY,YY,ZZ,ZZ,ZZ,
                ZZ,ZZ,YY,ZZ,YY,ZZ,ZZ,ZZ
                ]
        sense.set_pixels(BC)

# Lajva webbläsare
        agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36\(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        url = "https://www.kraken.com/charts"
# Ladda ner sida
        request = Request(url,headers={"User-Agent":agent})
        html = urlopen(request).read().decode()
        souped = soup(html,"html.parser")
# Skrapa data
        boxes = souped.findAll("div",{"class":"val mono"})
#        titles = ["Last","High","Low","Volume","Weight"]

#        call('clear')
#        print("    Kraken 24")
#        for i in range(len(boxes)):
#            print(titles[i],"\t",boxes[i]["data-val"])
# ^Fortsättning
        last = float(boxes[0]["data-val"])
        high = float(boxes[1]["data-val"])
        low = float(boxes[2]["data-val"])

# Sätt 'modes' som visar olika data med färg; en i taget
        H = { 
                1: [round(high),GG],
                2: [round(low),RR],
                3: [round(last),YY],
                4: [round(last-(high+low)//2),Cy]
                }

# Kör datan genom alla modes
        for i in range(4):
            D = H.get(next(mode))
            a,C = D[0],D[1]

# Ser huruvida talet är positivt/negativt
            if bin(a)[0]=="0":
                p = True
            else:
                p = False

# Skapar strängen som sen blir bilden; glömt
            img=""; revNr=str(abs(a))[::-1]

# Per siffra i talet; trimma binär affix, *
            for i in revNr:
                binary=bin(int(i))[2::]
# *Fyll rader med binära längd + kompletterande 0'or
                comp=8-len(binary)
                row="0"*comp+binary
                img+=row

# Kompletterande 0'or till resten av bilden och gör till Lista
            img = img+(64-len(img))*"0"
            img = list(img)

# Rotera90 1: matris (lista med listor), 2: reversera matrisen, 3: läs av columnvis, 4: "plana ut" listorna till en enda
            img = [img[i:i+8] for i in range(0,len(img),8)]
            img = img[::-1]
            img = zip(*img)
            img = [z for i in img for y in i for z in y]

# Ersätt alla tecken med Variabler { 1: G/R, 0: Z }
            for n,i in enumerate(img):
                if i=="1":
                    if p:
                        img[n]=C
                    else:
                        img[n]=Ne
                else:
                    img[n]=ZZ
# Vänster stapel
            img[0]=GG; img[56]=RR
            for i in range(8,32,8):
                img[i]=Cy
                img[i+24]=Ne
            L = round(((high-low)/(last-low)))%8
            L = 8*L
            img[L] = YY

            sense.set_pixels(img)

            zZz(8)

except KeyboardInterrupt:

    sense.clear()
    exit
