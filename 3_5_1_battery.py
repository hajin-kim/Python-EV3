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

# classmethod battery.voltage()
# 배터리의 전압을 가져옵니다.
# Returns 배터리 전압.
# Return type voltage: mV

# classmethod battery.current()
# 배터리에서 공급되는 전류를 가져옵니다.
# Returns 배터리 전류.
# Return type current: mA

# Play a warning sound when the battery voltage is below 7 Volt(7000 mV = 7V)
if ev3.battery.voltage() < 7000:    # voltage: 8300, current: 170
    ev3.speaker.beep()

