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

# classmethod screen.clear()
# 디스플레이의 모든 것을 지웁니다.
ev3.screen.clear()

# classmethod screen.draw_text(x, y, text)
# 텍스트를 표시합니다.
# Parameters
# • text(str) – 표시할 텍스트.
# • coordinate(tuple) –(x, y) 좌표 투플. 첫 번째 문자의 왼쪽 위 모서리를 지정합니다.
ev3.screen.draw_text(0, 0, "Hello,")
ev3.screen.draw_text(60, 20, "World!")

