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

# light(color)
# 브릭 라이트의 색상을 설정합니다.
# Parameters color(Color) – 라이트의 색상. 라이트를 끄려면 Color.BLACK 또는 None을 선택합니다.
#   you can choose one of these:
    # Color.BLACK
    # Color.BLUE
    # Color.BROWN
    # Color.GREEN
    # Color.ORANGE
    # Color.PURPLE
    # Color.RED
    # Color.WHITE
    # Color.YELLOW

# Make the light red
ev3.light.on(Color.RED)
# Wait in ms
wait(1000)
# Turn the light off
ev3.light.off()
