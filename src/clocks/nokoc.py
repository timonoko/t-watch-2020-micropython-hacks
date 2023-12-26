from micropython import const
from tempos import g, rtc, sched
from graphics import rgb, WHITE, BLACK, BLUE, CYAN, RED
from fonts import roboto24,roboto36
import array
import math
import png
from time import ticks_ms, ticks_diff


def drawRotRect(w, r1, r2, angle, c):
    w2, ll, a = w // 2, r2 - r1, (angle + 270) * (math.pi / 180)
    coord = array.array("h", [0, -w2, ll, -w2, ll, w2, 0, w2])
    x, y = math.ceil(g.width // 2 + r1 * math.cos(a)), math.ceil(
        g.height // 2 + r1 * math.sin(a)
    )
    g.poly(x, y, coord, c, True, a)


W = const(240)
H = const(240)
R = const(120)
CX = const(120)
CY = const(120)
GREY = rgb(220, 220, 220)
months = [
    "Tammi",
    "Helmi",
    "Maalis",
    "Huhti",
    "Touko",
    "Kesa",
    "Heina",
    "Elo",
    "Syys",
    "Loka",
    "Marras",
    "Joulu",
]
viikko= ["ma","ti","ke","to","pe","la","su"]
    
dialpic = png.getPNG("images/nokodial.png", WHITE)


def dialtext(text,x,y,big=False):
    ds = text
    if big: g.setfont(roboto36)
    else: g.setfont(roboto24)
    g.setfontalign(0, -1)
    g.setcolor(BLACK, WHITE)
    g.text(ds,x,y)
    
def dial(t):
    g.fill(WHITE)
    png.drawPNG(dialpic, 0, 0)
    dialtext(viikko[t[3]],20,0,True)
    dialtext("{:04}".format(t[0]),210,0)
    dialtext("{:02}".format(t[2]),20,220)
    dialtext(months[t[1] - 1],210,220)
    huu=t[4]%12
    if huu>2 and huu<10: dialtext("{:02}:{:02}".format(t[4],t[5]),120,65,True)
    if huu<4 or huu>8: dialtext("{:02}:{:02}".format(t[4],t[5]),120,145,True)
    if huu<1 or huu>5: dialtext("{:02}:{:02}".format(t[4],t[5]),170,120-12)
    if huu>11 or huu<7: dialtext("{:02}:{:02}".format(t[4],t[5]),70,120-12)

def secH(a, c):
    drawRotRect(2, 3, R - 10, a, c)


def minH(a, c):
    drawRotRect(6, 0, R - 10, a, c)


def hourH(a, c):
    drawRotRect(15, 0, R - 50, a, c)


def onSecond():
    SD = rtc.datetime()
    # begin = ticks_ms()
    dial(SD)
    hourH(SD[4] * 30 + SD[5] // 2, BLACK)
    minH(SD[5] * 6, BLUE)
    g.ellipse(CX, CY, 6, 6, BLACK, True)
    secH(SD[6] * 6, RED)
    g.ellipse(CX, CY, 3, 3, RED, True)
    g.show()
    # print("onSecond = ", ticks_diff(ticks_ms(),begin))


ticker = None


def app_init():
    global SD, ticker
    SD = rtc.datetime()
    onSecond()
    ticker = sched.setInterval(1000, onSecond)


def app_end():
    sched.clearInterval(ticker)
    g.setcolor(WHITE, BLACK)
    g.fill(BLACK)
