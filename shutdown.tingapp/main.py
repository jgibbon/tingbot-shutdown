import tingbot
from tingbot import *
from subprocess import call


@every(seconds=1.0)
def loop():
    # drawing code here
    screen.image(
        'bg.png',
        xy=(160, 120))

@left_button.press
def press():
    print 'left'
    call(["sudo", "halt"])

@right_button.press
def press():
    print 'right'
    call(["sudo", "reboot"])
    


tingbot.run()
