# Opens webrepl-port for 30 seconds
# you can acceess Repl by hitting control-C after logging in.

from tempos import g
from graphics import WHITE, BLACK, YELLOW
from fonts import roboto18, roboto24, roboto36
from button import Button, ButtonMan
import time
from widgets import Label
from wifi import do_connected_action
import math
import os
import webrepl

status = Label(10, 80, 180, 40, roboto24, YELLOW)
progress = Label(200, 80, 40, 40, roboto24, YELLOW)

def centre_text(str, font, x, y, c):
    global g
    g.setfont(font)
    g.setfontalign(0, -1)
    g.text(str, x, y, c)

def webr2():
    status.update("Running 30s")
    webrepl.start()
    time.sleep(30)
    
def webreplstart():
    global status, progress
    do_connected_action(webr2, status, progress)

update = Button("Start", 80, 180, 80, 40, roboto24)
buttons = ButtonMan()
buttons.add(update)
update.callback(webreplstart)

def app_init():
    global buttons
    centre_text("Webrepl", roboto36, 120, 4, WHITE)
    status.update("Idle")
    progress.update("")
    buttons.start()

def app_end():
    buttons.stop()
    g.fill(BLACK)
