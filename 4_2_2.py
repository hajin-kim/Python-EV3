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
# Initialize the Ultrasonic Sensor. It is used to detect
# obstacles as the robot drives around.
obstacleSensor = UltrasonicSensor(Port.S3)

# Write your program here.
ev3.speaker.beep()

while True:
    wait(10)
    if obstacleSensor.distance() < 300:
        ev3.speaker.beep()
        wait(900)


