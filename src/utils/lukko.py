# Omatekeman Wifi-lukon avaaja ref: https://github.com/timonoko/Lukko_ja_Ovikello

from tempos import g
from graphics import WHITE, BLACK, YELLOW, RED
from fonts import roboto18, roboto24, roboto36
from button import Button, ButtonMan
import time
from widgets import Label
from wifi import do_connected_action
from urequests import request
import math
import json
import os

status = Label(10, 80, 180, 40, roboto24, YELLOW)
progress = Label(200, 80, 40, 40, roboto24, YELLOW)

def curl(url):
    try: request("GET", url)
    except: print("pikku virhe")

def centre_text(str, font, x, y, c):
    global g
    g.setfont(font)
    g.setfontalign(0, -1)
    g.text(str, x, y, c)

def AU_KI():
    status.update("AU")
    curl("http://192.168.1.117/au")
    status.update("KI")
    curl("http://192.168.1.117/ki")
    status.update("AUKI")
    time.sleep(1)

def avaa_ovi():
    global status, progress
    do_connected_action(AU_KI, status, progress)

update = Button("AVAA", 80, 180, 80, 40, roboto24)
buttons = ButtonMan()
buttons.add(update)
update.callback(avaa_ovi)

def app_init():
    global buttons
    centre_text("O V  I", roboto36, 100, 10, RED)
    status.update("KIINNI")
    progress.update("")
    buttons.start()

def app_end():
    buttons.stop()
    g.fill(BLACK)
