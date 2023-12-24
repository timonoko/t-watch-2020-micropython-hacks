from tempos import g
from graphics import WHITE, BLACK, YELLOW, RED, GREEN, BLUE
from fonts import roboto18, roboto24, roboto36
from button import Theme, RoundButton, ButtonMan
from widgets import Label
import time
from wifi import do_connected_action
from urequests import request
import math
import os

status = Label(10, 60, 180, 40, roboto24, YELLOW)
progress = Label(200, 60, 40, 40, roboto24, YELLOW)

def curl(url):
    try: request("GET", url)
    except: print("pikku virhe")

def act_on(): curl("http://192.168.1.64/5/on")
def act_off(): curl("http://192.168.1.64/5/off")
      
        
def centre_text(str, font, x, y, c):
    global g
    g.setfont(font)
    g.setfontalign(0, -1)
    g.text(str, x, y, c)
    
def action(s):
    global status, progress
    status.update("OK")
    progress.update("")
    if s == "ON": do_connected_action(act_on,status,progress)
    elif s == "OFF": do_connected_action(act_off,status,progress)
    else: print('vaara nappi')

buttons = ButtonMan()
       
def butt(s,x,y,c):
    b = RoundButton(s,x,y,60,60,theme=Theme(BLUE,c,GREEN,c,roboto24))
    buttons.add(b)
    b.callback(action, s)

butt("ON",30,120,GREEN)
butt("OFF",130,120,RED)
    
def app_init():
    global buttons
    centre_text("NAPPI 64", roboto36, 80, 10, WHITE)
    buttons.start()

def app_end():
    buttons.stop()
    g.fill(BLACK)
