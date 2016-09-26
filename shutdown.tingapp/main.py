import tingbot
from tingbot import *
from subprocess import call
from os import environ

call_args = ""
call_on_next_tick = ""

def init():
    screen.fill(color=(0, 0, 0))
    setText("Press left button to shut down or right button to reboot")
    setImages("")

def runOnTingbot(systemcall, text):
    global call_on_next_tick
    if "TB_RUN_ON_LCD" not in environ:
        setText(text + "\n(This won't work if you're not running it on a tingbot.)")
        return
    if text:
        setText(text)
    call_on_next_tick = systemcall

def setText(txt):
    print txt
    screen.rectangle(size=(320,40), color=(0,0,0), align="bottom", xy=(screen.width/2, screen.height-10))
    screen.text(txt, color="white", align="bottom", font_size=9, xy=(screen.width/2, screen.height-10))


def setImages(mode):
    if(mode == "h"):
        screen.image("ico_h_active.png", align="topleft", xy=(10,10))
    else:
        screen.image("ico_h.png", align="topleft", xy=(10,10))

    if(mode == "r"):
        screen.image("ico_r_active.png", align="topright", xy=(screen.width-10, 10))
    else:
        screen.image("ico_r.png", align="topright", xy=(screen.width-10, 10))

@left_button.press
def press():
    setImages("h")
    runOnTingbot(["sudo", "shutdown", "-h", "now"], "You can unplug the power soon after the display turned white.")

@right_button.press
def press():
    setImages("r")
    runOnTingbot(["sudo", "reboot"], "See you soon!")

init()
screen.brightness = 100

@every(seconds=0.05)
def loop():
    # if called directly, the screen changes don't get through fast enough :/
    global call_args, call_on_next_tick
    
    if call_args != "":
        call(call_args)
        call_args = ""
    elif call_on_next_tick != "":
        call_args = call_on_next_tick
        call_on_next_tick = ""
    

tingbot.run()
