#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

# buttons()
# 현재 EV3 브릭의 어떤 버튼이 눌러졌는지 확인합니다.
# Returns 누른 버튼의 list that can be empty or contain
    # Button.BEACON
    # Button.CENTER
    # Button.DOWN
    # Button.LEFT
    # Button.LEFT_DOWN
    # Button.LEFT_UP
    # Button.RIGHT
    # Button.RIGHT_DOWN
    # Button.RIGHT_UP
    # Button.UP
#   Return type: list

# Do something if the left button is pressed
if Button.LEFT in ev3.buttons.pressed():
    ev3.speaker.beep(1000,500)
    print("The left button is pressed.")

print(ev3.buttons.pressed())
# TODO: Let's try with the interactive shell!

# dir(Button)
