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
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)

# Write your program here.
ev3.speaker.beep()

while True:
    inp = input("방향 입력:")
    if inp == 'w':
        leftMotor.run(200)
        rightMotor.run(200)
    elif inp == 's':
        leftMotor.stop()
        rightMotor.stop()
    elif inp == 'a':
        leftMotor.run(100)
        rightMotor.run(200)
    elif inp == 'd':
        leftMotor.run(200)
        rightMotor.run(100)
    elif inp == 'x':
        leftMotor.run(-50)
        rightMotor.run(-50)
