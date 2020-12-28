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

# classmethod speaker.beep(frequency=500, duration=100)
# 비프음/음향을 재생합니다.
# Parameters
# • frequency(frequency: Hz) – 비프음의 주파수 (Default: 500).
# • duration(time: ms) – 비프음의 길이 (Default: 100).

# A simple beep
ev3.speaker.beep()

# Wait in ms
wait(1000)

# A high pitch(1500 Hz) for one second(1000 ms) at 50% volume
ev3.speaker.set_volume(50) # in percentage
ev3.speaker.play_file(SoundFile.READY)

# dir(SoundFile)
